import base64
parola_dosya=open("parola.txt","r")
parola=parola_dosya.readline()
parola_dosya.close()
print parola
print base64.b64decode(parola)