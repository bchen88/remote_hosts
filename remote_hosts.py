#all the imports required
import asyncio
import asyncssh
import signal
import sys
from sys import argv

#define string array of hosts and command
hosts = []
cmd = ' '

#define loop
loop = asyncio.get_event_loop()

#parsing the command line arguments
def main():
    if len(argv) < 3:
        print("Invalid args!")
        print("Usage: python3 multiple_clients.py <one or more IPs> <a single command>")
        sys.exit(0)

    print('number of arguments=%d' % len(argv))

    # print command line arguments and store them in the hosts array
    for arg in sys.argv[1:]:
        print('argument=%s' % arg)

        #don't store the command in the hosts array
        if arg != sys.argv[len(argv)-1]:
            hosts.append(arg)
        else:
            cmd = arg

    # print the stored arguments
    for j in range(len(hosts)):
        print('host=%s, %d' % (hosts[j], j))

    print('command=%s' % cmd)

    #return the hosts and command set in this function
    return hosts, cmd

#connect to the remote host and run a single command
async def run_client(host, command):
#@asyncio.coroutine
#def run_client(host, command):
    async with asyncssh.connect(host) as conn:
#     @asyncio.coroutine with asyncssh.connect(host) as conn:
        return await conn.run(command)

#connect to the multiple remote hosts and run a single command on each host
async def run_multiple_clients(hosts, cmd):
    # Put your lists of hosts here
    #hosts = ['10.145.103.35', '10.145.103.36', '10.145.103.37', '10.145.103.33']

    tasks = (run_client(host, cmd) for host in hosts)
    #tasks = (run_client(host, 'ls -la') for host in hosts)
    #tasks = (run_client(host, 'sleep 10') for host in hosts)
    # schedule tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print('Task %d failed: %s' % (i, str(result)))
        elif result.exit_status != 0:
            print('Task %d exited with status %s:' % (i, result.exit_status))
            print(result.stderr, end='')
        else:
            print('Task %d succeeded:' % i)
            print(result.stdout, end='')

        print(50*'=')

#signal SIGINT handler
def signal_handler(signal, frame):
    print('Receive signal %d:' % signal)
    print('Program exiting')
    loop.stop()
    sys.exit(0)

#catch SIGINT signal
signal.signal(signal.SIGINT, signal_handler)

#normal process
try:
    if __name__ == "__main__":
       hosts, cmd = main()

    loop.run_until_complete(run_multiple_clients(hosts, cmd))
    loop.close()

#exception
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))
