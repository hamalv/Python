import datetime
import os 
import time

mysql_username = 'Root'
mysql_password = 'pa55word'

db_exclude = 'sys performance_schema information_schema'




################################ Date & Time ################################
def date_now():
    d = datetime.datetime.now()
    date = d.strftime("%Y.%m.%d")
    return date

def time_now():
    t = datetime.datetime.now()
    time = t.strftime("%H:%M:%S")
    return time

################################ Mysql backup ################################
def do_mysql_backup():
    time_start = time_now()
    date_start = date_now()
    
    print('===================================================================') 
    print(f'Starting Mysql backup\nTime: {time_start}\nDate: {date_start}\n\n ')
    
    time.sleep(2)
    os.system(f'mysqldump -u {mysql_username} -p  ')
    
    end_time = time_now()
    end_date = date_now()
    print(f'\n\nMysql backup finished\nTime: {end_time}\nDate: {end_date}')
    print('===================================================================') 




################################ Main ################################
def main():
    # Main function
    do_mysql_backup()

if __name__ == "__main__":
    main()
