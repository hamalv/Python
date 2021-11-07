import os

def main():
    # with open('test.txt', mode='r') as f:
    #     filedata = f.read()

    # filedata = filedata.replace('datadir=/var/lib/mysql', 'datadir=/data/mysql')    
    
    # with open('test.txt', mode='w') as f:
    #     f.write(filedata)

    # with open('test.txt', mode='r') as f:
    #     print(f.read())
    # f.close()
    # f.close()
    # f.close()
    with open('test.txt', mode='r') as f:
        for line in f:
            if 'A temporary password is generated' in line:
                print(line)

if __name__ == "__main__":
    main()
