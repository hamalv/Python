import os
import subprocess

def main():
    current_user = subprocess.check_output('whoami', shell=True).decode().strip()
    print(f"Current user: {current_user}")
    print("Trying login as root")
    # os.system("sudo su -")
    subprocess.run(["sudo su -"])

if __name__ == "__main__":
    main()
