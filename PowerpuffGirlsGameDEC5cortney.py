# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:25:37 2019

@author: Cortney
"""

import random

     
def diceRoll(play):
    min = 2
    max = 18 #when testing my function... i played with the min and max so that I would roll a "2" everytime
    if play == "y":
        rollValue = random.randint(min, max)
        print("You rolled", rollValue, "!")
    elif play == "n":
        print("Okay, Game over!")
    return rollValue

play = input("Would you like to roll the dice? Enter 'y' or 'n'. ")
while play not in {'y', 'n'}:
    play = input("Try again! ")
    
numberOfLives = 4

def rollValue2():
    print("Elmer, your classmate at Pokey Oaks Kindergarten, is eating paste and all the kids are teasing him. Buttercup even throws a ball of paste at his face! \n He gets cleaned up and sent outside to play by the teacher, but he sits under a tree with his jar of paste.")
    print("Meanwhile, a fly inside a garbage truck eats off a napkin from a nearby Marshmallow Toxic Filter Site and becomes radioactive!")
    print("The garbage truck drives by Pokey Oaks and the fly ends up in Elmer's paste. Elmer accidentally eats it and becomes a giant monster, made of glue!!!")
    print("...")
    print("He is tearing up the town, and everything is sticking to him!")
    glueOption = input("What should we do? \n Enter 1 to Fight! \n Enter 2 to apologize. ")
    while glueOption not in {'1', '2'}: #the easiest way to validate input i found
        glueOption = input("Enter 1 to Fight or 2 to apologize. ")
    if glueOption == "1":
        print("You get stuck in Elmer's glue. Instead of fighting him, you should have apologized! You lose one life.")
        global numberOfLives
        numberOfLives -= 1
        return numberOfLives
    elif glueOption == "2":
        print("Elmer accepts your apology! You saved the town and don't lose any lives!")

    
rollValue = diceRoll(play)
if rollValue == 2:
    rollValue2()
print(numberOfLives, "lives left.") #THIS IS JUST SO WE CAN SEE HOW MANY LIVES, to validate

'''
elif rollValue == 3:
    rollValue3()
elif rollValue == 4:
    rollValue4()
elif rollValue == 5:
    rollValue5()
elif rollValue == 6:
    rollValue6()
elif rollValue == 7:
    rollValue7()
elif rollValue == 8:
    rollValue8()
elif rollValue == 9:
    rollValue9()
elif rollValue == 10:
    rollValue10()
elif rollValue == 11:
    rollValue11()   
elif rollValue == 12:
    rollValue12()
elif rollValue == 13:
    rollValue13()
elif rollValue == 14:
    rollValue14()
elif rollValue == 15:
    rollValue15()
elif rollValue == 16:
    rollValue16()
elif rollValue == 17:
    rollValue17()
elif rollValue == 18:
    rollValue18()  
    
    

def rollValue3():
def rollValue4():
def rollValue5():
def rollValue6():
def rollValue7():
def rollValue8():
def rollValue9():
def rollValue10():
def rollValue11():
def rollValue12():
def rollValue13():
def rollValue15():
def rollValue16():
def rollValue17():
def rollValue18():

'''    