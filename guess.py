import numpy as np
from numpy import random
#top text of game
n="GUESS THE NUMBER GAME"
print(n)
#Generate a random target number between 1 and 50
target=random.randint(1,50)
while True:
# Asking the player for input
    userchoice=input("guess the target or QUIT(Q):")
 # If player enters 'Q', then the game will end 
    if(userchoice=="Q"):
        break
    userchoice=int(userchoice)
 # Compare guesses
    if(userchoice<target):
        print("The Number Is Small. choose some big number")
    elif(userchoice==target):
        print("The Number Is Found")
        break
    else:
        print("The Number is Large.choose some small number")   
   
                       