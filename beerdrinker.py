#####################################
###  Testing v1
###  a=bab2501 v= 1.0 d= 2018.12.08
####################################

###
# Dependencies
# => pip install requests
#########################
import requests
import time

###
# Global Settings
#########################

host = "dsbank.online"
protocol = "https"
port = "443"
baseurl = protocol + "://" + host + ":" + port

###
# Standard Functions (theAPI)
#########################
def createAccount(accountNumber):
        url = baseurl+"/accounts/create"
        jdata={"accountNumber": str(accountNumber)}
        r = requests.post(url,json=jdata)
        print("Status: " + str(r.status_code) + " Message: " + r.text + " -- createAccount " + str(accountNumber))

def balanceAccount(accountNumber):
        url = baseurl+"/accounts/"+str(accountNumber)+"/balance"
        #print(url)
        #jdata={"amount" : str(amount)}
        #r = requests.post(url,json=jdata)
        r = requests.get(url)
        print("Status: " + str(r.status_code) + " Message: " + r.text)
        #return float(r.text);

def depositAccount(accountNumber, amount):
        url = baseurl+"/accounts/"+str(accountNumber)+"/deposit"
        jdata={"accountNumber," : str(accountNumber), "amount" : amount}
        #print(url)
        r = requests.post(url,json=jdata)
        print("Status: " + str(r.status_code) + " Message: " + r.text + " -- depositAccount " + str(amount) + " to " + str(accountNumber))

def withdrawAccount(accountNumber, amount):
        url = baseurl+"/accounts/"+str(accountNumber)+"/withdraw"
        jdata={"amount" : amount}
        #print(url)
        r = requests.post(url,json=jdata)
        print("Status: " + str(r.status_code) + " Message: " + r.text + " -- withdrawAccount " + str(amount) + " from " + str(accountNumber))

def transferAccount(accountNumber, amount, accountNumberDestination):
        url = baseurl+"/accounts/"+str(accountNumber)+"/transfer"
        jdata={"amount" : amount, "accountNumberDestination" : str(accountNumberDestination)}
        #print(url)
        r = requests.post(url,json=jdata)
        print("Status: " + str(r.status_code) + " Message: " + r.text + " -- transferAccount " + str(amount) + " from " + str(accountNumber) + " to " + str(accountNumberDestination))

import socket
import time

def hostid():
		hostname = socket.gethostname()
		hostid = int(hostname[-2:])
		return hostid

# Get salary
depositAccount(99, 1)
desk = hostid()
cafe = (hostid() + 1)
depositAccount(desk, 10000)
depositAccount(cafe, 10000)

# Drink beer ( pay 2 from me(5) to cafebank(4) )
while True:
	print(time.time())
	for x in range(200):
		transferAccount(desk, 1, cafe)
	print(time.time())
	time.sleep(15)
		
		
		
		