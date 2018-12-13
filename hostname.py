import socket
import time
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
	if(mnow() < 5):
		print("now")
	print(mnow())
	time.sleep(1)
