import requests
import json
url="https://www.btcturk.com/api/ticker"
btcturk_sonuc=requests.get(url=url,verify=False).json()
print btcturk_sonuc[0]['last']
if int(btcturk_sonuc[0]['last'])>50000:
    print "50 milyardan buyuk"
url="https://rest.nexmo.com/sms/json"
payload={"api_key = 534c0667","api_secret=e6fb7c5d4006147b","to":"905438858037","from":"BTCTURK","text":"alma"}
requests.post(url=url,data=payload,verify=False)



