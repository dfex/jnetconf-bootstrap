jnetconf-bootstrap
==============

Programatically enable netconf over SSH on Junos devices.  Prepares network infrastructure for the use of PyEZ etc. 

### Requirements

- Paramiko
- Common username and password/SSH key across devices.  

### Usage

Pass a text file containing device IPs (one per line), and the script will log in via SSH and append:

```
set system services netconf ssh
```

to each device.

```
./jnetconf-bootstrap.py test-sample.csv

jnetconf-bootstrap

Username: bdale
Password (leave blank to use SSH Keys): 

. - success
x - error
Reading device list: .No handlers could be found for logger "paramiko.hostkeys"
....x
172.16.10.254 - completed
172.16.10.253 - completed
10.0.254.10 - completed
10.0.255.6 - completed
10.0.255.4 - completed
abc,IP Address Error - ignored
```
