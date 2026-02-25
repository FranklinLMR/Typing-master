import random
import re
import requests 
import time 
import sys
import keyboard
from termcolor import colored, cprint   
from time import sleep


#Machine writting function with enter

def typeoa(text, retraso=0.1, color=None, on_color = None, attrs= None):
    for letra in text:

        crdl= letra
        if color or on_color or attrs:
            crdl= colored(letra, color=color,on_color=on_color, attrs=attrs)
        sys.stdout.write(crdl)
        sys.stdout.flush()
        sleep(retraso)
    print()


#Machine writting function without enter

def typeob(text, retraso=0.1, color=None, on_color = None, attrs= None):
    for letra in text:

        crdl= letra
        if color or on_color or attrs:
            crdl= colored(letra, color=color,on_color=on_color, attrs=attrs)
        sys.stdout.write(crdl)
        sys.stdout.flush()
        sleep(retraso)



#Setting a marging to make it more clean
for f in range(0,100):
    print("")



#Retrieving the API

Mozambique= requests.get("https://random-word-api.herokuapp.com/word?number=25")



#General Index for everything we gonna retrieve from the API data

index= 0



#Extracting the data of the API and verifying everything's working (User-Sever relationship)
if Mozambique.status_code == 200:
    data= Mozambique.json()
else:
    print("this is not working")



#Round of words without input (first showcase)

typeob(f"{data[index]}", 0.01, color="yellow", on_color="on_dark_grey")
typeob(f" ", 0)
for f in range(index+1,len(data)):
    typeob(f"{data[f]} ", 0.01)



#Input, round of words with indications of validity

try:
    while index != 25:
            for x in range(0,10):
                print("")
            
            lol= input("\n")
            if lol == data[index]:
                index+=1
                for x in range(0,100):
                    print("")
                for l in range(0, index):
                    typeob(f"{data[l]}", 0.0001, on_color="on_green")
                    typeob(f" ", 0)
                typeob(f"{data[index]}", 0.01, color="yellow", on_color="on_dark_grey")
                typeob(f" ", 0)
                for f in range(index+1,len(data)):
                    typeob(f"{data[f]} ", 0.001)
            else:
                for x in range(0,100):
                    print("")
                if index != 0:
                    for l in range(0, index):
                        typeob(f"{data[l]}", 0.0001, on_color="on_green")
                        typeob(f" ", 0)
                    
                    typeob(f"{data[index]}", 0.0001, on_color="on_red")
                    typeob(" ",0)

                else:
                    typeob(f"{data[index]}", 0.0001, on_color="on_red")
                    typeob(f" ", 0)
                for f in range(index+1,len(data)):
                    typeob(f"{data[f]} ", 0.0001)
        
except:
    typeob("Well done", 0.05, color= "yellow")
    typeob("...",0.5)
    typeoa("You have succesfully completed the round of words in around:",0.05)


crr=time.time()

print(crr)


print(' '.join(data))