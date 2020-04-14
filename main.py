import os


os.system("clear")
os.system("tput setaf 1")
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
        print("PAckage Management\n")
        print("""\t\tPRESS 1 FOR INSTALLING A PROGRAMME
                 PRESS 2 FOR DELETING A PROGRAMME
                 PRESS 3 FOR SEARCHING A PROGRAMME
                 PRESS 4 FOR REPOSITORY MANAGEMENT""")
        ch2=input("Enter your choice: ")
        if int(ch2)==1 :
            var=input("Enter the programme you want to install: ")
            os.system("dnf install {}".format(var))
        elif int(ch2)==2 :
            var=input("Enter the name of programme you want to delete: ")
            os.system("dnf remove {}".format(var))
        elif int(ch2)==3 :
            var=input("Enter the programme you want to search: ")
            os.system("rpm -qa | grep {}".format(var))
        elif int(ch2)==4 :
            print("""PRESS 1 FOR ADDING REPOSITORIES
                     PRESS 2 FOR LISTING REPOSITORIES""")
            ch2_4=input("Enter your choice: " )
            if int(ch2_4)==1:
                print("""PRESS 1 FOR ADDING REPOS DRECTLY THROUGH DNF
                         PRESS 2 FOR ADDING REPOS TROUGH CONFIG FILE""")
                ch2_4_1=input("Enter your choice: ")
                if int(ch2_4_1)==1:
                    var=input("Enter the URL: ")
                    os.system("dnf install {}".format(var))
                elif int(ch2_4_1)==2:
                    os.chdir("/etc/yum.repos.d/")
                    os.system("/bin/bash")
                    os.system("gedit TUI_created.repo")
            elif int(ch2_4)==2:
                os.system("dnf repolist")



    elif int(ch)==3:
        #to check storage(lecture 28 & 29)
        print("Disk Maangement")
    elif int(ch)==4:
        #ip,to check ping to particular ip,to check details of connected devices
        print("networking")
    elif int(ch)==5:
        #to configure,to put files on webserver
        print("Webserver")
    elif int(ch)==6:
        #to trsnsfer files through scp
        print("Files Transfer")
    else :
        print("INPUT NOT SUPPORTED")

elif location == "remotely":                      #if location remotely
    print("Enter the IP of remote host")
    remoteIp = input()
    auth = input("""Do You want to do Key authentication YES/NO""")  #if key authenticaton is required
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
        print("PAckage Management\n")
        print("""\t\t\tPRESS 1 FOR INSTALLING A PROGRAMME
                 PRESS 2 FOR DELETING A PROGRAMME
                 PRESS 3 FOR SEARCHING A PROGRAMME
                 PRESS 4 FOR REPOSITORY MANAGEMENT""")
        ch2=input("Enter your choice: ")
        if int(ch2)==1 :
            var=input("Enter the programme you want to install: ")
            os.system("dnf install {}".format(var))
        elif int(ch2)==2 :
            var=input("Enter the name of programme you want to delete: ")
            os.system("dnf remove {}".format(var))
        elif int(ch2)==3 :
            var=input("Enter the programme you want to search: ")
            os.system("rpm -ia | grep {}".format())
        elif int(ch2)==4 :
            print("""PRESS 1 """)






    elif int(ch)==3:
        #to check storage(lecture 28 & 29)
        print("Disk Maangement")
    elif int(ch)==4:
        #ip,to check ping to particular ip,to check details of connected devices
        print("networking")
    elif int(ch)==5:
        #to configure,to put files on webserver
        print("Webserver")
    elif int(ch)==6:
        #to trsnsfer files through scp
        print("Files Transfer")
    else :
        print("INPUT NOT SUPPORTED")
