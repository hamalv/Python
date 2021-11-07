import os
import subprocess

# Unix
servlist    = '/home/jfreiber/gitlab/jfreiber/python/vmsnap/servlist'
vmsnap_log  = '/var/log/vmsnap/vmsnap_mysql.log'

username = 'jfreiber'

def list_servlist():
    host_list=[]
    with open(servlist) as hosts:
        print("\n\n")
        for host in hosts:
            if not host.startswith("#"):
                host_list.append(host.strip())
    return host_list

def read_log(line):
    date    = line.strip()[:10]
    time    = line.strip()[11:19]
    msg     = line.strip()[20:]
    print(f"Date: {date}")
    print(f"Time: {time}")
    print(f"Msg: {msg}")

def main():
    hosts = list_servlist()
    print(hosts)
    print("_________________________________ Servlist Done _________________________________")

    for host in hosts:
        print("________________")
        cmd = 'tail -1 /var/log/vmsnap/vmsnap_mysql.log'
        result = subprocess.Popen("ssh {username}@{host} {cmd}".format(username=username, host=host, cmd=cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log_last_line   = result.stdout.read().strip().decode('utf-8')
        log_error       = result.stderr.read().strip().decode('utf-8')

        if log_error != '':
            print(f"Error: {log_error}")
        else:
            print(f"Error: No errors")
            print(f"Host: {host} \nLog: {log_last_line}")
            read_log(log_last_line)

        print("________________")

    print("\n\n")

if __name__ == "__main__":
    main()