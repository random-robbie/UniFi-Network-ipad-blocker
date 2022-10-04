#!/usr/bin/env python
#
# 
#
# 
#
# By @Random-Robbie
# 
# Yes i am aware this is a bit naff but feel free to submit PR.
#
#
#
import requests
import sys
import argparse
import os.path
import re
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()


#### config ###
username = ""
password = ""
server = ""


def login(mac,sta,username,password):
	rawBody = '{"username":"'+username+'","password":"'+password+'","remember":false,"strict":true}'
	headers = {"Origin":"https://"+server+":8443","Accept":"*/*","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0","Referer":"https://"+server+":8443/manage/account/login?redirect=%2Fmanage","Connection":"close","Sec-Fetch-Dest":"empty","Sec-Fetch-Site":"same-origin","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"cors","Te":"trailers","Accept-Language":"en-US,en;q=0.5","Content-Type":"application/json; charset=utf-8"}
	response = session.post("https://"+server+":8443/api/login", data=rawBody, headers=headers,verify=False)
	x = response.cookies["csrf_token"]
	if response.status_code == 200:
		rawBody2 = '{"mac":"'+mac+'","cmd":"'+sta+'"}'
		headers2 = {"Origin":"https://"+server+":8443","Accept":"*/*","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0","Referer":"https://"+server+":8443/manage/site/default/clients/1/50","Connection":"close","Sec-Fetch-Dest":"empty","Sec-Fetch-Site":"same-origin","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"cors","Te":"trailers","Accept-Language":"en-US,en;q=0.5","Content-Type":"application/json; charset=utf-8","X-Csrf-Token":x}
		response2 = session.post("https://"+server+":8443/api/s/default/cmd/stamgr", data=rawBody2, headers=headers2,verify=False)
		if response2.status_code == 200:
			print("Action Complete")
		else:
			print("Failed")

		
		
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--child", required=True ,help="Childs Name")
parser.add_argument("-s", "--state", required=True ,help="block or unblock")
args = parser.parse_args()

child = args.child
ub = args.state

if child == "molly":
	mac = "20:0d:38:90:02:f0"
if child == "tom":
	mac = "8b:cb:4b:d2:ed:13"

if ub == "block":
	sta = "block-sta"
else:
	sta = "unblock-sta"
	
login(mac,sta,username,password)
