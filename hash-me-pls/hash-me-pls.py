import requests
from bs4 import BeautifulSoup
import hashlib
from datetime import datetime
import browser_cookie3
import re

start = datetime.now()

url = "https://ringzer0ctf.com/challenges/13"
cookies = browser_cookie3.firefox(domain_name='ringzer0ctf.com')

login_data={"PHPSESSID":""}

for cookie in cookies:
    if cookie.domain == "ringzer0ctf.com":
        login_data["PHPSESSID"]=cookie.value
print("Cookie: "+str(login_data))
print("\n")
 
req=requests.get(url, cookies=login_data)

soup = BeautifulSoup(req.text,'html.parser')

msg = soup.find_all(class_="message")[0].get_text()
result = msg.replace("----- BEGIN MESSAGE -----","").replace("----- END MESSAGE -----","").strip()

bytee = bytes(result, "utf-8")

hex_dig = hashlib.sha512(bytee).hexdigest()

print("HASH "+result)
print("SHA512 "+str(hex_dig)+"\n")

req = requests.post(url+"/"+str(hex_dig), cookies=login_data)
elapsed = datetime.now() - start

if "Wrong answer or too slow" not in req.text:
    grep = re.search("FLAG-\w+", req.text)
    print("\nFLAG:"+grep.group(0))
    print("Challenge is done!")
print("Elapsed time: "+str(elapsed))
