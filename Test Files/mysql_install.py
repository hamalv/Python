import datetime
import subprocess 
import os
import time

answer_yes = ['y','Y','Yes','yes']

################ Date & Time ################
def date_now():
    d = datetime.datetime.now()
    date = d.strftime("%Y.%m.%d")
    return date

def time_now():
    t = datetime.datetime.now()
    time = t.strftime("%H:%M:%S")
    return time

################ Passwords ################
def request_password(mode):
    if mode == 'user':
        #password = input("Password: ")
        password = 'pa55word'
    return password

################ Scripts ################
def check_mysql_version():
    os.system("yum info mysql-community-server | grep 'Name\|Arch\|Version\|Release\|Size'")

def script_start():
    time_start = time_now()
    time_st = time.perf_counter()
    date_start = date_now()
    print(f'\n\nStarting Mysql install\nTime: {time_start}\nDate: {date_start}')
    print('===================================================================')
    return time_st

def script_end(time_st, mode, error_msg=" "):
    time_end = time_now()
    time_en = time.perf_counter()
    date_end = date_now()
    print('===================================================================') 

    if mode == 'sucess':
        print(f'Mysql install finished sucessfully\nTime: {time_end}\nDate: {date_end}')
        print(f'Time elapsed: {time_en - time_st:0.2f} seconds')

    elif mode == 'error':
        print(f'[Error] {error_msg}\nTime: {time_end}\nDate: {date_end}')

def make_dir():
    os.system('rm -rf /data/mysql')
    path = "/data/mysql"
    access_rights = 0o755
    try:
        os.mkdir(path, access_rights)
    except OSError:
        print(f"Failed to create directory at: {path}")
    else:
        print(f"Directory created successfully at: {path}")

def edit_mycnf_file():
    mycnf = '/etc/my.cnf'
    file = open(mycnf, mode='r')
    data = file.read()
    data = data.replace('datadir=/var/lib/mysql', 'datadir=/data/mysql')
    file.close()
    file = open(mycnf, mode='w')
    file.write(data)
    file.close()

def cat_mysql_password():
    log_file = '/var/log/mysqld.log'
    with open(log_file, mode='r') as f:
        for line in f:
            if 'A temporary password is generated' in line:
                print(line)


################################ Mysql install ################################
def do_mysql_install():
    check_mysql_version()
    con = input("Continue installing? [Y/N]")
    if con not in answer_yes:
        script_end('error', 'Mysql instalation cancelled by user.')
    else:
        time_st = script_start()
        current_user = subprocess.check_output('whoami', shell=True).decode().strip()

        if current_user != 'root':
            print(f"I'm not root. I'm loged in as {current_user}")
            script_end('error', 'Login error: user is not logged as root')
            
        else:
            print("I'm root user")
            make_dir()
            #os.system('yum -y install mysql-community-server')
            edit_mycnf_file()
            
            script_end(time_st, 'sucess')
            print("-------------------------------------------------------------------")
            os.system('systemctl start mysqld')
            time.sleep(4)
            cat_mysql_password()
            os.system('mysqlsh --py -e "select * from mysql.users;"')
            #os.system("create user 'jfreiber'@'localhost' identified by RootJan_5")




################################ Main ################################
def main():
    do_mysql_install()

if __name__ == "__main__":
    main()
