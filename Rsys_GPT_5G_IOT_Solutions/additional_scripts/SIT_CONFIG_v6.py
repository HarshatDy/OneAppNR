import paramiko
import getpass
import time
import os
import re 


#General Configuration 
vendor_name=["vendorA_ORUAA100_FR1918010111"]
ip_pre="172.27."

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



def configuration(main_dirName, ip, vendor_name): 
    du_file_name=[]
    dirName_arr = [
    main_dirName,
    main_dirName+'/rsysfs/opt/radisys/cu/config',
    main_dirName+'/rsysfs/opt/radisys/du/config',
    main_dirName+'/rsysfs/opt/radisys/platform-services/system-mgr/configs',
    main_dirName+'/rsysfs/opt/radisys/platform-services/system-mgr/scripts',
    main_dirName+'/rsysfs/opt/radisys/platform-services/procmon/config',
    main_dirName+'/rsysfs/opt/radisys/platform-services/netconf_server',
    main_dirName+'/rsysfs/opt/radisys/oam-services/netconf_client/oam_du/config',
    main_dirName+'/rsysfs/opt/radisys/oam-services/netconf_client/oam_cu/config',
    main_dirName+'/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/',
    main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/",
    main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/",
    main_dirName+"/mnt/metadata",
    main_dirName+"/etc" ]
    #main_dirName+"/opt/radisys/platform-services/system-mgr/configs/"   ]
    for dir in dirName_arr:
        try:
            # print(dir)
            # Create target Directory
            os.makedirs(str(dir))
            print("Directory " , dir ,  " Created ")
        except FileExistsError:
            print("Directory " , dir ,  " already exists")

    port=22
    username='ognb'
    #password=getpass.getpass()
    password="ognb123"
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password, allow_agent=False)
    sftp_client=ssh.open_sftp()
    print("****************Backup Started***************")
    #CU Oid
    sftp_client.get("/rsysfs/opt/radisys/cu/config/mem_config.txt" , "./"+main_dirName+"/rsysfs/opt/radisys/cu/config/mem_config.txt")
    sftp_client.get("/rsysfs/opt/radisys/cu/config/sys_config.txt" , "./"+main_dirName+"/rsysfs/opt/radisys/cu/config/sys_config.txt")
    sftp_client.get("/rsysfs/opt/radisys/oam-services/netconf_client/oam_cu/config/oam_3gpp_netconf_gnb_cu_push.sh" , "./"+main_dirName+"/rsysfs/opt/radisys/oam-services/netconf_client/oam_cu/config/oam_3gpp_netconf_gnb_cu_push.sh")
    with open('./'+main_dirName+'/rsysfs/opt/radisys/oam-services/netconf_client/oam_cu/config/oam_3gpp_netconf_gnb_cu_push.sh') as t:
        for line in t :
            pattern = '/opt/radisys/oam-services/netconf_client/(.*\.xml)'
            reg = re.search(pattern, line)
            if reg: 
                pattern1 = '/config/(.*\.xml)'
                reg1 = re.search(pattern1, reg.group(1))
                filename = reg1.group(1)
                # exit(0)
                sftp_client.get(reg.group() , "./"+main_dirName+"/rsysfs/opt/radisys/oam-services/netconf_client/oam_cu/config/"+filename)

    print("CU Backup Done")
    #L2
    sftp_client.get("/rsysfs/opt/radisys/du/config/mem_config.txt" , "./"+main_dirName+"/rsysfs/opt/radisys/du/config/mem_config.txt")
    sftp_client.get("/rsysfs/opt/radisys/du/config/sys_config.txt" , "./"+main_dirName+"/rsysfs/opt/radisys/du/config/sys_config.txt")
    sftp_client.get("/rsysfs/opt/radisys/oam-services/netconf_client/oam_du/config/oam_3gpp_odu_push.sh" , "./"+main_dirName+"/rsysfs/opt/radisys/oam-services/netconf_client/oam_du/config/oam_3gpp_odu_push.sh")
    with open('./'+main_dirName+'/rsysfs/opt/radisys/oam-services/netconf_client/oam_du/config/oam_3gpp_odu_push.sh') as t:
        for line in t :
            pattern = '/opt/radisys/oam-services/netconf_client/(.*[^$oru_vendor]\.xml)'
            reg = re.search(pattern, line)
            if reg:
                pattern1 = '/config/(.*\.xml)'
                reg1 = re.search(pattern1, reg.group(1))
                du_file_name.append(reg.group(1))
    #           print(du_file_name)
                sftp_client.get(reg.group() , "./"+main_dirName+"/rsysfs/opt/radisys/oam-services/netconf_client/oam_du/config/"+reg1.group(1))
    with open('./'+main_dirName+'/rsysfs/opt/radisys/oam-services/netconf_client/'+du_file_name[2]) as t:
        for line in t :
            pattern = '<id>(.*)<\/id>'
            reg = re.search(pattern,line)
            if reg:
                if reg.group(1) == vendor_name[0] :
                    sftp_client.get("/opt/radisys/oam-services/netconf_client/oam_oru_cntrl/config/oam_oran_3_oru_conf.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/oam-services/netconf_client/oam_du/config/oam_oran_3_oru_conf.xml")           
    #            else:
    #                print("Need ORU VENDOR NAMES")
                
    print("L2 Backup Done")

    #l1
    #sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/xrancfg_sub6_SysConfig.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/xrancfg_sub6_SysConfig.xml")
    #sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/xrancfg_sub6_SwConfig.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/xrancfg_sub6_SwConfig.xml")
    #sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_sysCfg.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_sysCfg.xml")
    # sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_filtered.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1//phycfg_xran_filtered.xml")
    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_sysCfg.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_sysCfg.xml")
    with open("./"+main_dirName+"/rsysfs/opt/radisys/du/config/sys_config.txt") as t:
        for line in t:
            pattern =       'L1_INSTANCE_INFO= {.*,.*,(.*)}.*{.*,.*,(.*)}'
            pattern_single ='L1_INSTANCE_INFO=\s*{.*,.*,(.*)}'
            # print(line)
            reg2 = re.search(pattern_single,line)
            reg = re.search(pattern,line)
            #print(reg2.group())
            #print(" LI INSTANCE " + reg.group(1))
            if reg :
                print(reg.group())
                if(reg.group(2) == "TDD"):
                    #print(" COPYING TDD FILES" )
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/xrancfg_sub6_SysConfig.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/xrancfg_sub6_SysConfig.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/phycfg_xran_sysCfg.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/phycfg_xran_sysCfg.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/l1.sh","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/l1.sh")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_filtered_TDD.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1//phycfg_xran_filtered_TDD.xml")
                if(reg.group(1) == "FDD"):
                    #print(" COPYING FDD FILES" )
                    ftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/xrancfg_sub6_SysConfig.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/xrancfg_sub6_SysConfig.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/phycfg_xran_sysCfg.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/phycfg_xran_sysCfg.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/l1.sh","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/l1.sh")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_filtered_FDD.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1//phycfg_xran_filtered_FDD.xml")      
            if reg2 :
                print(reg2.group())
                if(reg2.group(1)=="TDD"):
                    #print("Copying SINGLE TDD")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/xrancfg_sub6_SysConfig.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/xrancfg_sub6_SysConfig.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/phycfg_xran_sysCfg.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/phycfg_xran_sysCfg.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/l1.sh","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb1/l1.sh")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_filtered_TDD.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1//phycfg_xran_filtered_TDD.xml")
                if(reg2.group(1)=="FDD"):
                    #print("Copying SINGLE FDD")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/xrancfg_sub6_SysConfig.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/xrancfg_sub6_SysConfig.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/phycfg_xran_sysCfg.xml","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/phycfg_xran_sysCfg.xml")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/l1.sh","./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/orancfg/sub6_mu0_10mhz_sub6_mu1_100mhz/gnb0/l1.sh")
                    sftp_client.get("/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1/phycfg_xran_filtered_FDD.xml" , "./"+main_dirName+"/rsysfs/opt/radisys/l1/bin/nr5g/gnb/l1//phycfg_xran_filtered_FDD.xml")      
 
    print("L1 Backup Done")
        #Platforma
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/configs/gen2_interface.cfg" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/configs/gen2_interface.cfg")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/configs/xr11_interface.cfg" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/configs/xr11_interface.cfg")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/configs/sync_mgr_ognb.cfg" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/configs/sync_mgr_ognb.cfg")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/configs/oam_platform_sys_mgr_du_confd_cfg.txt" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/configs/oam_platform_sys_mgr_du_confd_cfg.txt")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/scripts/configure_odu.py" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/scripts/configure_odu.py")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/scripts/setup_eth.py" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/scripts/setup_eth.py")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/procmon/config/service_config.json" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/procmon/config/service_config.json")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/procmon/config/oam_process_monitor_confd_cfg.txt" , "./"+main_dirName+"/rsysfs//opt/radisys/platform-services/procmon/config/oam_process_monitor_confd_cfg.txt")
    sftp_client.get("/mnt/metadata/interface_configs.xml" , "./"+main_dirName+"/mnt/metadata/interface_configs.xml")
    sftp_client.get("/mnt/metadata/eventapi_confd_cfg.txt" , "./"+main_dirName+"/mnt/metadata/eventapi_confd_cfg.txt")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/configs/xr11_interface.cfg" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/configs/xr11_interface.cfg")
    sftp_client.get("/rsysfs/opt/radisys/platform-services/system-mgr/configs/gen2_interface.cfg" , "./"+main_dirName+"/rsysfs/opt/radisys/platform-services/system-mgr/configs/gen2_interface.cfg")
    sftp_client.get("/etc/.product.txt" , "./"+main_dirName+"/etc/product.txt")
    print("Platform Backup Done")
    print("configuration backup done!!!!!")



def main():
    while(1):
        print("**************************************************")
        option=input("Do you want to take backup of all Setups? (y/n) \n************************************************** \n")
        
        if option=='y': 
            print("**************************************************")
            dir_name=input("Please Enter the folder name where the config will be copied \n************************************\n")
            for ip in setup_ip :
                print("**************************************************")
                print("Started backup for " + ip_pre+ip + " Setup :  \n************************************************** \n")
                configuration(dir_name+"/"+ip_pre+ip , ip_pre+ip , vendor_name)
            break
        elif option=='n': 
            print("**************************************************")
            dir_name=input("Please Enter the folder name where the config will be copied \n************************************\n")
            print("**************************************************")
            main_dirName = input("Please enter the Setup ip and Meta Version \n************************************************** \n")
            while(1):
                print("**************************************************")
                ip=input("Enter the SIT setup ip-addr (IPV4): \n************************************************** \n")
                if re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$', ip.lower()):
                    print("Correct IP")
                    break
                else:
                    print("INVAILD IP ADDR !!")
            configuration(dir_name+"/"+main_dirName,ip,vendor_name)
            break
        else : 
            print("**************************************************")
            print("Please type y for yes or n for no \n************************************************** \n")
    exit(0)
    

if __name__ == '__main__':
    main()

        
