import os


os.system("tput setaf 5")
print("\t\t\t\t\tTUI")
os.system("tput setaf 7")
print("\t\t\t_______________________________")


print("""\t PRESS 1 for BASIC OPERATIONS   
         PRESS 2 for PACKAGE MANAGEMENT
         PRESS 3 for DISK MANAGEMENT
         PRESS 4 for NETWORKING
         PRESS 5 for WEBSERVER MANAGEMENT
         PRESS 6 for FILE TRANSFER""")

location=input("Where do you want to perform operations remotely/locally :")     #to check for location
if location == "locally":
    print("ENTER YOUR CHOICE :",end="")
    ch=input()

    if int(ch)==1:
        #basic commands
        os.system("clear")
        print("""PRESS 1 SEARCH PROGRAMME
             PRESS 2 RUNNING PROGRAMS
             PRESS 3 SEARCH FILES OR DIRECTORIES
             PRESS 4 FILE AND DIRECTORY MANAGEMENT
             PRESS 5 USER MANAGEMENT""")
        print("ENTER YOUR CHOICE :",end="")
        ch1=input()

        if int(ch1)==1:
            #to search programme
            print("To search programme")
        elif int(ch1)==2:
            #to see running programmes
            print("to see running programmes")
        elif int(ch1)==3:
            #to search files or directories
            print("to search files or diretories")
        elif int(ch1)==4:
            #to add,del,list etc. files and directory
            print("file management")
        elif int(ch1)==5:
            #to add,del,list,change password etc. users
            print("USer management")
        else :
            print("Input Not Supported")
        


    elif int(ch)==2:
        #to install,delete,add repos programmes
        print("PAckage Management")
    elif int(ch)==3:
        #to check storage(lecture 28 & 29)
        print("Disk Maangement")
    elif int(ch)==4:
        #ip,to check ping to particular ip,to check details of connected devices
        print("networking")
    elif int(ch)==5:
        #to configure,to put files on webserver
        
        print("""1.CONGFIGURE WEBSERVER                                     2.CREATE AND SAVE WEBPAGES""")

        WSCH = int(input("enter your choice: "))  
        
        if WSCH==1:
            os.system("dnf install httpd")                             os.system("systemctl enable httpd")                        os.system("systemctl disable firewalld")               
        elif WSCH==2:                                                  os.system("cd DIRECTORY_ROOT") #JUST ADD DIRECTORY ROOT BY CHECKING  FROM httpd.conf file IN DIRECTORY/etc/httpd/conf 
            file_name = input("enter file name: ")
            os.system("vim file_name")
        
        else :
            print("invalid choice")
             
    elif int(ch)==6:
        #to trsnsfer files through scp
        print("Files Transfer")
    else :
        print("INPUT NOT SUPPORTED")

elif location == "remotely":                                                #if location remotely
    print("Enter the IP of remote host")
    remoteIp = input()
    auth = input("""Do You want to do Key authentication YES/NO:""")         #if key authenticaton is required
    if auth == "YES":
        #genertate and send key to remoteIp
        print("Key Transfer")

    print("ENTER YOUR CHOICE :",end="")
    ch=input()

    if int(ch)==1:
        #basic commands
        os.system("clear")
        print("""PRESS 1 SEARCH PROGRAMME
             PRESS 2 RUNNING PROGRAMS
             PRESS 3 SEARCH FILES OR DIRECTORIES
             PRESS 4 FILE AND DIRECTORY MANAGEMENT
             PRESS 5 USER MANAGEMENT""")
        print("ENTER YOUR CHOICE :",end="")
        ch1=input()

        if int(ch1)==1:
            #to search programme
            print("To search programme")
        elif int(ch1)==2:
            #to see running programmes
            print("to see running programmes")
        elif int(ch1)==3:
            #to search files or directories
            print("to search files or diretories")
        elif int(ch1)==4:
            #to add,del,list etc. files and directory
            print("file management")
        elif int(ch1)==5:
            #to add,del,list,change password etc. users
            print("USer management")
        else :
            print("Input Not Supported")
        


    elif int(ch)==2:
        #to install,delete,add repos programmes
        print("PAckage Management")
    elif int(ch)==3:
        #to check storage(lecture 28 & 29)
        print("Disk Maangement")
    elif int(ch)==4:
        #ip,to check ping to particular ip,to check details of connected devices
        print("networking")
    elif int(ch)==5:
        #to configure,to put files on webserver

        print("""1.CONGFIGURE WEBSERVER
        2.CREATE AND SAVE WEBPAGES""")

        WSCH = int(input("enter your choice: "))

        if WSCH==1:
            os.system("dnf install httpd")
            os.system("systemctl enable httpd")
            os.system("systemctl disable firewalld")

        elif WSCH==2:
            os.system("cd DIRECTORY_ROOT") #JUST ADD DIRECTORY ROOT BY CHECKING  FROM httpd.conf file IN DIRECTORY/etc/httpd/conf
            file_name = input("enter file name: ")
            os.system("vim file_name")

        else:
            print("invalid option")
            
    elif int(ch)==6:
        #to trsnsfer files through scp
        print("Files Transfer")
    else :
        print("INPUT NOT SUPPORTED")
