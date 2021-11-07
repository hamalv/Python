import os
import subprocess
import getpass
import paramiko


######### Global Variables #########
conn_port = 22
servlist    = '/home/jfreiber/gitlab/jfreiber/python/del_old_bck/servlist2'
mysql_script = '/var/spool/ltk_scheduler/mysql'
username = getpass.getuser()
password = getpass.getpass("Your password: ")



######### Functions #########
def conn(host, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, conn_port, username, password, timeout=10)
    try:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.readlines()
    except:
        result = 'error'
    return result


def conn_with_pw(host, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, conn_port, username, password, timeout=10)
    ssh.get_transport()
    try:
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
        stdin.write(password + '\n')
        stdin.flush()
        result = stdout.readlines()
    except:
        result = 'error'
    ssh.close()
    return result
   
        
def get_hosts():
    host_list = []
    with open(servlist) as hosts:
        print("\n")
        for host in hosts:
            if not host.startswith("#"):
                host_list.append(host.strip())
    return host_list


def get_bck_dest(host):
    cmd = 'cat /var/spool/ltk_scheduler/mysql | grep "DEST="'
    try:
        result = conn(host, cmd)
    except:
        result = 'error'
    return result


def remove_files_from(host, location):
    loc = location[6:-1]
    cmd = 'sudo rm -rf ' + loc + '/*.sql.gz'
    print(f'| Command:              {cmd}')
    try:
        result = conn_with_pw(host, cmd)
    except:
        result = 'error'
    return result





######### Main #########
def main():
    hosts = get_hosts()
    print('|------------------------------------------------------')
    print(f"| Hosts list: {hosts}")
    print(f"| Total hosts: {len(hosts)}")
    for host in hosts:
        print('|------------------------------------------------------')
        err = 0
        bck_dest = get_bck_dest(host)
        if bck_dest == 'error':
            bck_dest = "!!! --- Error: Couldn't get backup location --- !!!"
        else:    
            try:
                bck_dest = bck_dest[0].rstrip()
            except:
                bck_dest = "!!! --- Error:Don't have backup dest --- !!!"
            #bck_dest = bck_dest[0].rstrip()
            # rm_file = remove_files_from(host, bck_dest)
            # if rm_file == 'error':
            #     rm_file = "!!! --- Error: Couldn't remove backup --- !!!"
            # else:
            #     rm_file = "Files removed succesfully"

        print(f"| Hostname:             {host}")
        print(f"| Backup location:      {bck_dest}")
        # print(f"| Action:               {rm_file}")
    print('|------------------------------------------------------')       
    print("\n")


if __name__ == "__main__":
    main()