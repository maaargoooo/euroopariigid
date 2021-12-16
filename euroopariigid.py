from module1 import *
f=open("TextFile1.txt","r")
riigid=[]
for line in file:
    k,v=line.strip().split("-")
    riigid[k.strip()]=v.strip()
z=""
while True:
    z=input("Что бы ты хотел сделать?\nСтраны и его столицы - 1\n - Тест")