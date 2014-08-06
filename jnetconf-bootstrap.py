#!/usr/bin/env python

## jnetconf-bootstrap.py - 06/08/2014
## ben.dale@gmail.com
## Automated Junos NETCONF over SSH enablement
## 

import sys
import time
import re
import paramiko
from getpass import getpass

sys.stdout.write("jnet-bootstrap\n\n")
if len(sys.argv) != 2:
	sys.stdout.write("Error: Missing parameter\n")
	sys.stdout.write("Usage: jnet-bootstrap <hostlist.csv>\n")
	sys.exit()
	
user = raw_input('Username: ')
passwd = getpass('Password (leave blank to use SSH Key): ')
sys.stdout.write(". - success\n")
sys.stdout.write("x - error\n")

deviceInventory = []

# Regex for routable IP addresses (1.0.0.0-223.255.255.255)
inetRegex = re.compile("^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-1][0-9]|22[0-3])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$") 

sys.stdout.write("Reading device list: ")
sys.stdout.flush()
hostsfile = open(str(sys.argv[1]),'r')
for hostAddress in hostsfile:
	if inetRegex.match(str(hostAddress)):
		sys.stdout.write('.')
		sys.stdout.flush()
		deviceConnection = paramiko.SSHClient()
		deviceConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		if passwd != '':
			deviceConnection.connect(hostAddress.rstrip('\n'),username=user)
		else:
			deviceConnection.connect(hostAddress.rstrip('\n'),username=user,password=passwd)
		deviceShell = deviceConnection.invoke_shell()
		deviceShell.send("configure\n")
		deviceShell.send("set system services netconf ssh\n")
		deviceShell.send("commit and-quit\n")
		time.sleep(10)
		deviceConnection.close()
		sys.stdout.write("o")
		sys.stdout.flush()
	else:	
		sys.stdout.write("x")
		sys.stdout.flush()