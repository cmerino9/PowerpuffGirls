# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:25:37 2019

@author: Cortney
"""

import random

     
def diceRoll(play):
    min = 2
    max = 18
    if play == "y":
        rollValue = random.randint(min, max)
        print("You rolled", rollValue, "!")
    elif play == "n":
        print("Okay, Game over!")
        
    #return rollValue ... might have to return rollValue to add to total spaces moved

play = input("Would you like to roll the dice? Enter 'y' or 'n'. ")
while play not in {'y', 'n'}:
    play = input("Try again! ")
    
diceRoll(play)


'''
if rollValue == 2:
    rollValue2()
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
    
    
def rollValue2():
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