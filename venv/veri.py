import requests
dosya=open("isim.txt","r")
dosya_icerik=dosya.readlines()
dosya.close()
for i in dosya_icerik:
    print i.split("\n")[0]
    url="http://192.168.199.130/"+str(i.split("\n")[0])
    sonuc=requests.get(url)
    print sonuc