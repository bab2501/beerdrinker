import socket
import time
import os

def hostid():
	hostname = socket.gethostname()
	hostid = int(hostname[-2:])
	return hostid

def tnow():
	return int(time.time())

def mnow():
	return (tnow() %900 )

print(tnow())
print(mnow())
print(hostid())

while True:
	if(mnow() < 4):
		print(mnow)
		os.system("pkill -f beerdrinker.py")
		time.sleep(5)
		print(mnow)
		os.system("git reset --hard master") 
		time.sleep(5)
		os.system("git pull") 
		time.sleep(10)
                print(mnow)
                os.system("python beerdrinker.py&")
	print(mnow())
	time.sleep(1)
