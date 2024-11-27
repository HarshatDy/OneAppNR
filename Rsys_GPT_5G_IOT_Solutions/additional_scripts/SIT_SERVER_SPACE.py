import paramiko
import getpass
import os
import re 


pre_ip="172.27."

#Please add all the setup IP in the below array for backup
setup_ip=[
#Setup#24-LIONS
    "186.56",
#X2RU Setup
    "21.27",
#Setup#1-PrismaP1
    "1.4",
#Setup#2-PrismaP2
    "21.18",
#Setup#22
    "21.52",
#Setup#23
    "21.53",
#Setup#13-Radiated Setup
    "186.2",
#Setup#21-Radiated Setup
   # "21.66",
#Setup#5 RAFT
    "21.10",
#Benetel
    "22.17",
#NEC
    "186.45",
#Seyup#10
    "186.23",
#Seyup#11
    "186.76"
    ]




for ip in setup_ip:

    ip=pre_ip+ip
    remote_path="/"
    port=22
    username='ognb'
    #password=getpass.getpass()
    password="ognb123"
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(f"df -h")
    output = stdout.read().decode()
    errors = stderr.read().decode()

    print(f" **********************************Space in {ip} server*********************************");
    print("Output:\n", output)
    if errors:
        print("Errors:\n", errors)

