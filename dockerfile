#run python 3.6.3
FROM python:3.6

#arguments
ARG ssh_prv_key
ARG ssh_pub_key

#install asyncssh
RUN python3.6 -m pip install --upgrade pip
RUN python3.6 -m pip install asyncssh

# Authorize SSH Hosts
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan 10.145.103.35 >> /root/.ssh/known_hosts && \
    ssh-keyscan 10.145.103.35 >> /root/.ssh/known_hosts && \
    ssh-keyscan 10.145.103.36 >> /root/.ssh/known_hosts && \
    ssh-keyscan 10.145.103.37 >> /root/.ssh/known_hosts && \
    ssh-keyscan 10.145.103.33 >> /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

# Remove SSH keys
#RUN rm -rf /root/.ssh/

ADD remote_hosts.py /

ENTRYPOINT ["python3", "remote_hosts.py"]
