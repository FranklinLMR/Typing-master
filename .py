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




crr=time.time()

print(crr)


print(' '.join(data))