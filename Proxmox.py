#!/bin/python3
import os
import sys
import argparse
from subprocess import call


parser = argparse.ArgumentParser(description='Use Proxmox server by API REST')
parser.add_argument('--node',dest='NODE',type=str,help='Name of node on server')
parser.add_argument('--url',dest='URI',type=str,help='Url for serveur Proxmox (http://10.5.51.2/api2/json)')
parser.add_argument('--machine-type',dest='TYPE',type=str,help='Virtual machine type\t1) : lxc\t2) : qemu')
parser.add_argument('-m',dest='CHOICE',type=int,help='Choice of action \t1) : Shutdown\t2) : Status\t3) : Start')
parser.add_argument('-u',dest='USERNAME',type=str,help='Username for connect to server')
parser.add_argument('-r',dest='REALM',type=str,help='Realm for user on Proxmox')
parser.add_argument('-p',dest='PASSWORD',type=str,help='Password for connection to server')

args = parser.parse_args()


# Test if in args list have only himself
if len(sys.argv) <= 1 :
    parser.print_help()
    print("\nExemple : "+sys.argv[0] + " --machine-type 1 --node lpcc3 -m 2 -u root -r pam -p poulpe ")

# # Test if type of machine 1=lxc || 2=qemu
# if args.TYPE == 1 : 
#     type = "lxc"
# else :
#     type = "qemu"

# Test if noode is not define
if args.NODE == "" :
    os.exit()

# Test choice of user for post request on Proxmox server
if args.CHOICE == 1 : 
    #Shutdown
    call(["curl", "--silent", "--cookie", "$(<cookie)", "--headers", "$(<csrftoken)",  "-X",  "POST", args.URI+args.NODE+"/"+args.TYPE+"/"])
elif args.CHOICE == 2 :
    #Status
    call(["curl", "--silent", "--cookie", "$(<cookie)", "--headers", "$(<csrftoken)",  "-X",  "POST", args.URI+args.NODE+"/"+type+"/"])
elif args.CHOICE == 3 :
    #Start
    call(["curl", "--silent", "--cookie", "$(<cookie)", "--headers", "$(<csrftoken)",  "-X",  "POST", args.URI+args.NODE+"/"+type+"/"])

