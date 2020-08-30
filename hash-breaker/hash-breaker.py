import requests
from bs4 import BeautifulSoup
import hashlib
from datetime import datetime
import browser_cookie3
import re

start = datetime.now()

url = "https://ringzer0ctf.com/challenges/56"

#cookies = browser_cookie3.firefox(domain_name='ringzer0ctf.com')

login_data={"PHPSESSID":"123456789asdcookie"}

# for cookie in cookies:
#     if cookie.domain == "ringzer0ctf.com":
#         login_data["PHPSESSID"]=cookie.value
# print("Cookie: "+str(login_data))
# print("\n")
 
req=requests.get(url, cookies=login_data)

soup = BeautifulSoup(req.text,'html.parser')

msg = soup.find_all(class_="message")[0].get_text()
result = msg.replace("----- BEGIN HASH -----","").replace("----- END HASH -----","").strip()

print("HASH MSG: "+result)

#Read generated hashes file
fopen = open("hashes.txt", "r")

pattern=r"\w+."+result

print("REGEX: "+pattern)

hex_dig = re.findall(pattern, fopen.read())

hex_dig = hex_dig[0]
print("Found: "+hex_dig)
cracked=hex_dig.split("=")[0]
print("Cracked: "+cracked)

solved_url=url+"/"+cracked
print("URL: {}".format(solved_url))
req = requests.post(solved_url, cookies=login_data)

soup = BeautifulSoup(req.text,'html.parser')

elapsed = datetime.now() - start

if "Wrong" not in req.text:
    grep = re.search("FLAG-\w+", req.text)
    print("\nFLAG:"+grep.group(0))
    print("Challenge is done!")
else:
    print(alert)
print("Elapsed time: "+str(elapsed))
