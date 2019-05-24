
remote_hosts.py command line to connect to multiple hosts over SSH and runs a command on all of them at the same time.

###Prerequisites:

Need to run python 3
stream the output from stdout and stderr from connected to the console.

Assume you have installed the latest docker-ce


Set up public authentication key via SSH on all remote hosts
#ssh-keygen
#ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.145.103.35
#ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.145.103.36
#ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.145.103.37
#ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.145.103.33


### Usage:

First build docker images

    docker build -t python-remote-hosts --build-arg ssh_prv_key="$(cat /root/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat /root/.ssh/id_rsa.pub)" .

Show docker images you just build

    docker images

### usage examples:

Sample info from the python 3 command

# python -V
Python 3.6.3

# python remote_hosts.py 10.145.103.35 10.145.103.36 10.145.103.37 10.145.103.33 'ls -la'
number of arguments=6
argument=10.145.103.35
argument=10.145.103.36
argument=10.145.103.37
argument=10.145.103.33
argument=ls -la
host=10.145.103.35, 0
host=10.145.103.36, 1
host=10.145.103.37, 2
host=10.145.103.33, 3
command=ls -la
Task 1 succeeded:
total 96
dr-xr-x---.  9 root root  4096 May 16 13:30 .
dr-xr-xr-x. 18 root root   253 Feb 13 15:46 ..
-rw-------.  1 root root  2348 Jan 24 13:46 anaconda-ks.cfg
-rw-------.  1 root root 14311 May 22 13:33 .bash_history
-rw-------.  1 root root  3999 Jan 30 14:32 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 25 17:24 .cache
drwx------.  7 root root    71 Jan 25 17:24 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 24 14:19 .dbus
-rw-r--r--.  1 root root  2448 Jan 24 14:22 initial-setup-ks.cfg
-rw-r--r--.  1 root root 32291 Jan 28 11:26 k8s_worker1_setup_logs
drwxr-xr-x.  2 root root     6 Jan 25 19:08 .kube
-rw-r--r--.  1 root root  2016 Feb 14 18:12 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 24 14:21 .local
-rw-r--r--.  1 root root  1089 Feb 12 15:57 nfs_setup_logs
drwxr-----.  3 root root    19 Jan 25 19:04 .pki
drwx------.  2 root root    29 May 22 13:29 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
-rw-------.  1 root root   848 Jan 29 11:51 .viminfo
==================================================
Task 2 succeeded:
total 136
dr-xr-x---.  8 root root  4096 May 22 14:09 .
dr-xr-xr-x. 17 root root   242 Feb 20 13:58 ..
-rw-------.  1 root root  2348 Jan 23 18:17 anaconda-ks.cfg
-rw-------.  1 root root  6379 Feb 20 17:29 .bash_history
-rw-------.  1 root root  3026 Jan 30 14:42 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 28 10:21 .cache
drwx------.  7 root root    71 Jan 28 10:21 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 23 18:20 .dbus
-rw-r--r--.  1 root root  2461 Jan 23 18:22 initial-setup-ks.cfg
-rw-r--r--.  1 root root 88453 Jan 28 11:29 k8s_worker2_setup_logs
-rw-r--r--.  1 root root  2015 Feb 14 18:22 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 23 18:21 .local
drwxr-----.  3 root root    19 Jan 28 10:45 .pki
drwx------.  2 root root    29 May 22 14:09 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
==================================================
Task 3 succeeded:
total 84
dr-xr-x---.  8 root root  4096 Feb 15 15:51 .
dr-xr-xr-x. 17 root root   242 Feb 20 13:58 ..
-rw-------.  1 root root  2336 Jan 23 17:51 anaconda-ks.cfg
-rw-------.  1 root root  5052 Feb 20 15:51 .bash_history
-rw-------.  1 root root  1795 Jan 30 14:41 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 28 18:06 .cache
drwx------.  6 root root    58 Jan 28 18:06 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 23 17:58 .dbus
-rw-r--r--.  1 root root  2449 Jan 23 18:08 initial-setup-ks.cfg
-rw-r--r--.  1 root root 34833 Jan 28 18:36 k8s_worker3_setup_logs
-rw-r--r--.  1 root root  2085 Feb 14 18:12 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 23 18:05 .local
drwxr-----.  3 root root    19 Jan 28 18:12 .pki
drwx------.  2 root root    29 May 22 14:07 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
==================================================
Task 4 succeeded:
total 80
dr-xr-x---.  8 root root  4096 Feb 14 18:07 .
dr-xr-xr-x. 17 root root   242 Feb 20 13:59 ..
-rw-------.  1 root root  2336 Jan 24 15:45 anaconda-ks.cfg
-rw-------.  1 root root  6256 Feb 20 15:50 .bash_history
-rw-------.  1 root root  2016 Jan 30 14:41 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 28 09:48 .cache
drwx------.  6 root root    58 Jan 28 09:48 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 24 16:17 .dbus
-rw-r--r--.  1 root root  2436 Jan 24 16:19 initial-setup-ks.cfg
-rw-r--r--.  1 root root 30855 Jan 28 18:33 k8s_worker4_setup_logs
-rw-r--r--.  1 root root  2873 Feb 14 18:07 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 24 16:18 .local
drwxr-----.  3 root root    19 Jan 28 18:24 .pki
drwx------.  2 root root    48 May 22 14:04 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
==================================================




Sample info from the docker command

# docker run python-remote-hosts 10.145.103.35 10.145.103.36 10.145.103.37 10.145.103.33 'ls -la'
number of arguments=6
argument=10.145.103.35
argument=10.145.103.36
argument=10.145.103.37
argument=10.145.103.33
argument=ls -la
host=10.145.103.35, 0
host=10.145.103.36, 1
host=10.145.103.37, 2
host=10.145.103.33, 3
command=ls -la
Task 1 succeeded:
total 96
dr-xr-x---.  9 root root  4096 May 16 13:30 .
dr-xr-xr-x. 18 root root   253 Feb 13 15:46 ..
-rw-------.  1 root root  2348 Jan 24 13:46 anaconda-ks.cfg
-rw-------.  1 root root 14311 May 22 13:33 .bash_history
-rw-------.  1 root root  3999 Jan 30 14:32 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 25 17:24 .cache
drwx------.  7 root root    71 Jan 25 17:24 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 24 14:19 .dbus
-rw-r--r--.  1 root root  2448 Jan 24 14:22 initial-setup-ks.cfg
-rw-r--r--.  1 root root 32291 Jan 28 11:26 k8s_worker1_setup_logs
drwxr-xr-x.  2 root root     6 Jan 25 19:08 .kube
-rw-r--r--.  1 root root  2016 Feb 14 18:12 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 24 14:21 .local
-rw-r--r--.  1 root root  1089 Feb 12 15:57 nfs_setup_logs
drwxr-----.  3 root root    19 Jan 25 19:04 .pki
drwx------.  2 root root    29 May 22 13:29 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
-rw-------.  1 root root   848 Jan 29 11:51 .viminfo
==================================================
Task 2 succeeded:
total 136
dr-xr-x---.  8 root root  4096 May 22 14:09 .
dr-xr-xr-x. 17 root root   242 Feb 20 13:58 ..
-rw-------.  1 root root  2348 Jan 23 18:17 anaconda-ks.cfg
-rw-------.  1 root root  6379 Feb 20 17:29 .bash_history
-rw-------.  1 root root  3026 Jan 30 14:42 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 28 10:21 .cache
drwx------.  7 root root    71 Jan 28 10:21 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 23 18:20 .dbus
-rw-r--r--.  1 root root  2461 Jan 23 18:22 initial-setup-ks.cfg
-rw-r--r--.  1 root root 88453 Jan 28 11:29 k8s_worker2_setup_logs
-rw-r--r--.  1 root root  2015 Feb 14 18:22 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 23 18:21 .local
drwxr-----.  3 root root    19 Jan 28 10:45 .pki
drwx------.  2 root root    29 May 22 14:09 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
==================================================
Task 3 succeeded:
total 84
dr-xr-x---.  8 root root  4096 Feb 15 15:51 .
dr-xr-xr-x. 17 root root   242 Feb 20 13:58 ..
-rw-------.  1 root root  2336 Jan 23 17:51 anaconda-ks.cfg
-rw-------.  1 root root  5052 Feb 20 15:51 .bash_history
-rw-------.  1 root root  1795 Jan 30 14:41 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 28 18:06 .cache
drwx------.  6 root root    58 Jan 28 18:06 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 23 17:58 .dbus
-rw-r--r--.  1 root root  2449 Jan 23 18:08 initial-setup-ks.cfg
-rw-r--r--.  1 root root 34833 Jan 28 18:36 k8s_worker3_setup_logs
-rw-r--r--.  1 root root  2085 Feb 14 18:12 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 23 18:05 .local
drwxr-----.  3 root root    19 Jan 28 18:12 .pki
drwx------.  2 root root    29 May 22 14:07 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
==================================================
Task 4 succeeded:
total 80
dr-xr-x---.  8 root root  4096 Feb 14 18:07 .
dr-xr-xr-x. 17 root root   242 Feb 20 13:59 ..
-rw-------.  1 root root  2336 Jan 24 15:45 anaconda-ks.cfg
-rw-------.  1 root root  6256 Feb 20 15:50 .bash_history
-rw-------.  1 root root  2016 Jan 30 14:41 bash_history
-rw-r--r--.  1 root root    18 Dec 28  2013 .bash_logout
-rw-r--r--.  1 root root   176 Dec 28  2013 .bash_profile
-rw-r--r--.  1 root root   176 Dec 28  2013 .bashrc
drwx------.  4 root root    31 Jan 28 09:48 .cache
drwx------.  6 root root    58 Jan 28 09:48 .config
-rw-r--r--.  1 root root   100 Dec 28  2013 .cshrc
drwx------.  3 root root    25 Jan 24 16:17 .dbus
-rw-r--r--.  1 root root  2436 Jan 24 16:19 initial-setup-ks.cfg
-rw-r--r--.  1 root root 30855 Jan 28 18:33 k8s_worker4_setup_logs
-rw-r--r--.  1 root root  2873 Feb 14 18:07 kubeadm-join
drwxr-xr-x.  3 root root    19 Jan 24 16:18 .local
drwxr-----.  3 root root    19 Jan 28 18:24 .pki
drwx------.  2 root root    48 May 22 14:04 .ssh
-rw-r--r--.  1 root root   129 Dec 28  2013 .tcshrc
==================================================

