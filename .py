import random
import re
import requests 
import time 
import sys
import keyboard
from termcolor import colored, cprint   
from time import sleep

def typeoa(text, retraso=0.1, color=None, on_color = None, attrs= None):
    for letra in text:

        crdl= letra
        if color or on_color or attrs:
            crdl= colored(letra, color=color,on_color=on_color, attrs=attrs)
        sys.stdout.write(crdl)
        sys.stdout.flush()
        sleep(retraso)
    print()

def typeob(text, retraso=0.1, color=None, on_color = None, attrs= None):
    for letra in text:

        crdl= letra
        if color or on_color or attrs:
            crdl= colored(letra, color=color,on_color=on_color, attrs=attrs)
        sys.stdout.write(crdl)
        sys.stdout.flush()
        sleep(retraso)

h=0
Mozambique= requests.get("https://random-word-api.herokuapp.com/word?number=25")

index= 0
if Mozambique.status_code == 200:
    data= Mozambique.json()
else:
    print("Hello World, ts is not working")

for f in range(index,len(data)):
    typeob(f"{data[f]} ", 0.01)

while True:
        lol= input("\n")
        if lol == data[index]:
            index+=1
            for x in range(0,100):
                print("")
            for l in range(0, index):
                typeob(f"{data[l]}", 0.01, on_color="on_green")
                typeob(f" ", 0)
            for f in range(index,len(data)):
                typeob(f"{data[f]} ", 0.01)
        else:
            for x in range(0,100):
                print("")
            if index != 0:
                for l in range(0, index):
                    typeob(f"{data[l]}", 0.01, on_color="on_green")
                    typeob(f" ", 0)
                
                typeob(f"{data[index]}", 0.01, on_color="on_red")
                typeob(" ",0)

            else:
                typeob(f"{data[index]}", 0.01, on_color="on_red")
                typeob(f" ", 0)
            for f in range(index+1,len(data)):
                typeob(f"{data[f]} ", 0.01)
    


crr=time.time()

print(crr)


print(' '.join(data))