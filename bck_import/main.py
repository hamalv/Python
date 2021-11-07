import os
import time
import datetime

# dir = '/data/backup/table_private/'
# bck_files = [
#     'dhcp_logs_private_p202009.sql'
#     ,'dhcp_logs_private_p202008.sql'
#     ,'dhcp_logs_private_p202007.sql'
# ]

dir2 = '/data/backup/table_public/'
bck_files2 = [
    # 'dhcp_logs_public_p202103.sql'
    # ,'dhcp_logs_public_p202102.sql'
    'dhcp_logs_public_p202101.sql'
    # ,'dhcp_logs_public_p202012.sql'
    # ,'dhcp_logs_public_p202011.sql'
    ,'dhcp_logs_public_p202010.sql'
    # ,'dhcp_logs_public_p202009.sql'
    # ,'dhcp_logs_public_p202008.sql'
    # ,'dhcp_logs_public_p202007.sql'
    # ,'dhcp_logs_public_p202006.sql'
    # ,'dhcp_logs_public_p202005.sql'
    # ,'dhcp_logs_public_p202004.sql'
    # ,'dhcp_logs_public_p202002.sql'
    # ,'dhcp_logs_public_p202001.sql'
    # ,'dhcp_logs_public_p201912.sql'
]


def main():
    # print(type(bck_files))
    # for i in bck_files:
    #     cmd = "date; mysql -u root -p'' logwatcher < " + dir + i + "; date;"
    #     d = "date;"
    #     print(f"-------------------------------------------------------")
    #     print(f"Command: {cmd}")
    #     os.system(cmd)
    #     time.sleep(5)

    for i in bck_files2:
        cmd = "date; mysql -u root -p'' logwatcher < " + dir2 + i + "; date;"
        d = "date;"
        print(f"-------------------------------------------------------")
        #print(f"DETAILS\nFile: {i}\nCommand: {cmd}")
        print(f"File: {i}")
        os.system(cmd)
        time.sleep(180)

if __name__ == "__main__":
    main()