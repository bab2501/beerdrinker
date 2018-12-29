#####################################
###  BT metric v1
###  a=bab2501 v= 1.0 d= 2018.12.29
####################################

###
# Dependencies
#########################
import socket
import time
import os

def hostid():
	hostname = socket.gethostname()
	return hostname
	
def hostname():
	hostname = socket.gethostname()
	hostid = int(hostname[-2:])
	return hostid

def tnow():
	return int(time.time())

def mnow():
	return (tnow() %300 )

print(tnow())
print(mnow())
print(hostname())

while True:
	if(mnow() < 4):
		print(mnow)
		os.system("start")
		time.sleep(5)
		print(mnow)
		os.system("date >> report.log")
		os.system("du -s /home/ablaauwgeers/.bitcoin >> report.log")
		os.system("date >> report.log")
	print(mnow())
	time.sleep(1)
print("end")