from gtts import gTTS
import os
sonastik={}
riigid=[]
linnad=[]
file=open("TextFile1.txt","r")
for line in file:
    k, v=line.strip().split("-")#Riik:Pealinn
    sonatik[k.strip()]=v.strip()
    riigid.append(k)
    linnad.append(sonatik[k.strip()])
file.close()
print(sonastik)
print("Riigid:")
print(riigid)
print("Pealinnad:")
print(linnad)
