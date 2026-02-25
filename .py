import requests 
import time 
import sys
from termcolor import colored   
from time import sleep


#Machine writting function with enter (also with color capabilities)

def typeoa(text, retraso=0.1, color=None, on_color = None, attrs= None):
    for letra in text:

        crdl= letra
        if color or on_color or attrs:
            crdl= colored(letra, color=color,on_color=on_color, attrs=attrs)
        sys.stdout.write(crdl)
        sys.stdout.flush()
        sleep(retraso)
    print()


#Machine writting function without enter (also with color capabilities)

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



typeob("Welcome", 0.05)
typeoa("...",1)

while True:
    typeoa("Type the amount of words you want to work with:", 0.05)

    try:
        chosen = int(input())

        break
    except:
        typeoa("That was not a number, try again", 0.08)
        for f in range(15):
            print("")


for h in range(100):
    print("")



#Retrieving the API


Mozambique= requests.get(f"https://random-word-api.herokuapp.com/word?number={chosen}")



#General Index for everything we gonna retrieve from the API data

index= 0


while True:
    #Extracting the data of the API and verifying everything's working (User-Sever relationship)
    if Mozambique.status_code == 200:
        data= Mozambique.json()
        break
    else:
        print("this is not working")
        



#Round of words without input (first showcase)

typeob(f"{data[index]}", 0.01, color="yellow", on_color="on_dark_grey")
typeob(f" ", 0)
for f in range(index+1,len(data)):
    typeob(f"{data[f]} ", 0.01)




mistake_counter = 0
#Starting a stopwatch
start_time= time.time()

#Input, round of words with indications of validity
while True:
        for x in range(0,10):
                print("")
            
        lol= input("\n")
        
        if index != (chosen-1):
            if lol == data[index]:
                index+=1
                typeoa("Correct!", 0.08, "green")
                sleep(1.5)
                for x in range(0,100):
                    print("")
                for l in range(0, index):
                    typeob(f"{data[l]}", 0, on_color="on_green")
                    typeob(f" ", 0)
                typeob(f"{data[index]}", 0, color="yellow", on_color="on_dark_grey")
                typeob(f" ", 0)
                for f in range(index+1,len(data)):
                    typeob(f"{data[f]} ", 0)
            else:
                typeoa("At least you tried...", 0.08, "red")
                sleep(1)
                typeoa("go again!", 0.05, "yellow")
                sleep(1.5)
                mistake_counter +=1
                for x in range(0,100):
                    print("")
                if index != 0:
                    for l in range(0, index):
                        typeob(f"{data[l]}", 0, on_color="on_green")
                        typeob(f" ", 0)
                    
                    typeob(f"{data[index]}", 0, on_color="on_red")
                    typeob(" ",0)

                else:
                    typeob(f"{data[index]}", 0, on_color="on_red")
                    typeob(f" ", 0)
                for f in range(index+1,len(data)):
                    typeob(f"{data[f]} ", 0)
        else:
            break

#Stopping our stopwatch

end_time = time.time()

for x in range(0,100):
    print("")
for l in range(0, index+1):
    typeob(f"{data[l]}", 0.0001, on_color="on_green")
    typeob(f" ", 0)
for f in range(10):
    print("")

sleep(1)
#Gathering time lapsed
time_lapsed = end_time - start_time

#Final message
typeob("Well done", 0.05, color= "yellow")
typeob("...", 1)
typeob("You have ",0.05, "yellow")
typeoa("succesfully completed the round of words in around:",0.05, "green")
typeob(f"{round(time_lapsed, 3)} seconds, ", 0.05, "cyan")
typeob(f"with a total of ", 0.05, "yellow")
typeoa(f"{mistake_counter} mistakes", 0.05, "red")
typeoa(f"With a {round((mistake_counter/chosen*100), 3)} % of accuracy")
sleep(3)
for h in range(10):
    print("")

typeoa("Im really tired so restart the code if you want to do it again :)", 0.05)
sleep(2)
typeoa("I do not want to deal with multiple while loops", 0.05)

