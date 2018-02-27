import requests
url="https://localhost:8834/session"
payload={"username":"ebusttk","password":"admin"}
sonuc=requests.post(url=url,data=payload,verify=False).json()
print sonuc
cookie="token="+str(sonuc['token'])
print cookie
header={"X-cookie":cookie}
url="https://localhost:8834/folders"
sonuc=requests.get(url=url,headers=header,verify=False).json()
for i in sonuc['folders']:
    print i['name']