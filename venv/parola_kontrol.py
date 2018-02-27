# -*- coding:utf-8 -*-
dosya=open("parolalar.txt","r")
dosya_icerik=dosya.readlines()
dosya.close()
print dosya_icerik
buyuk_harfler=["Q","W","R"]
kucuk_harfler=["o","t","a","d","m","i","n","z","x","s"]
sayilar=["1","2","3","4","5","6"]
sayi_sayici=0
buyuk_harf_sayici=0
kucuk_harf_sayici=0
toplam_harf=0

for i in dosya_icerik:
    print i
    for buyuk_harf in buyuk_harfler:
        toplam_harf+=1
        if buyuk_harf in i:
            buyuk_harf_sayici+=1
print "toplam büyük harf sayısı:",str(buyuk_harf_sayici)
print toplam_harf