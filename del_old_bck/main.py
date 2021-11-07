import os
import subprocess
import getpass

###### Windows
#servlist = 'C:/Users/jfreiber/OneDrive - SIA Tet/Desktop/GitLab_tet/jfreiber/python/del_old_bck/servlist'
###### Unix
servlist    = '/home/jfreiber/gitlab/jfreiber/python/del_old_bck/servlist'
mysql_script = '/var/spool/ltk_scheduler/mysql'

username = getpass.getuser()
password = getpass.getpass("Your password: ")



# def lines_that_equal(line_to_match, fp):
#     return [line for line in fp if line == line_to_match]
# def lines_that_contain(string, fp):
#     return [line for line in fp if string in line]
# def lines_that_start_with(string, fp):
#     return [line for line in fp if line.startswith(string)]
# def lines_that_end_with(string, fp):
#     return [line for line in fp if line.endswith(string)]
# def generate_lines_that_equal(string, fp):
#     for line in fp:
#         if line == string:
#             yield line

def get_hosts():
    host_list = []
    with open(servlist) as hosts:
        print("\n\n")
        for host in hosts:
            if not host.startswith("#"):
                host_list.append(host.strip())
    return host_list

def get_bck_dest(host):
    cmd = 'cat /var/spool/ltk_scheduler/mysql | grep "DEST="'
    conn = subprocess.Popen("sshpass -p '" + password + "' ssh {username}@{host} {cmd}".format(username=username, host=host, cmd=cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log_error = conn.stderr.read().strip().decode('utf-8')
    res = conn.stdout.read().strip().decode('utf-8')
    log_dest = res[6:-1]
    if log_error != '':
        print(f"!!! Error !!!\nHost: {host}\n{log_error}")
        result = 1
    else:
        print(f"No errors\nHost: {host}\nDest: {log_dest}")
        result = log_dest
    return result

def del_bck(host, dest):
    cmd = 'sudo rm -rf ' + dest + '/hugo.hugodb-test.08-04-2021.sql.gz'
    print(f"{cmd}")
    conn = subprocess.Popen("sshpass -p '" + password + "' ssh {username}@{host} {cmd}".format(username=username, host=host, cmd=cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).write(password)
    del_error = conn.stderr.read().strip().decode('utf-8')
    res = conn.stdout.read().strip().decode('utf-8')
    if del_error != '':
        print(f"Log error: {del_error}")
        return 1
    else:
        print(f"Result: {res}")
    



###################### Main ######################
def main():
    
    hosts = get_hosts()

    print(hosts)
    for host in hosts:
        err = 0
        print("\n")
        bck_dest = get_bck_dest(host)
        if bck_dest == 1:
            print(f"Host unreachable!")
        else:
            print(host)
            # del_result = del_bck(host, bck_dest)
            # if del_result == 1:
            #     print(f"Bck delete failed.")
            # else: 
            #     print(f"Bck delete finished successfully.")
            

if __name__ == "__main__":
    main()