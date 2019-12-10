# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:22:41 2019

@author: Cortney
"""

import random

#This function rolls the dice and validates input     
def diceRoll(play):
    min = 1
    max = 3
    if play == "y":
        rollValue = random.randint(min, max)
        print("You rolled", rollValue, "!")
    elif play == "n":
        print("Okay, Game over!")
    return rollValue

print("welcome intro message here, rules of game")   
#Ask the user which Powerpuff girl they would like to be, and validate input     
name = input("Which Powerpuff girl do you want to be? Bubbles, Buttercup, or Blossom? ")
while name not in {'Buttercup','buttercup',"Bubbles",'bubbles','Blossom','blossom'}:
    name = input("Not an eligible player... which Powerpuff girl do you want to be? \n Bubbles, Buttercup, or Blossom? ")

#Set initial lives to 4        
numberoflives = 4

#define function that lets the user know how they are doing
def lives():
    if numberoflives == 0:
        print("Game over!!", name, "and the rest of the Powerpuff Girls are no more, MOJO JOJO! >:(")
    #put break of code here to exit
    elif numberoflives == 4:
        print("Sugar, Spice, Everything Nice, and Chemical X... You have all 4 lives. You go girl!")
    elif numberoflives == 3:
        print("You have got three lives", name, "; Sugar, Spice, and everything nice. Chemical X is missing and ahhhh your powers are getting weaker...")
    elif numberoflives == 2:
        print("You have got two lives", name, "; Sugar and Spice, keep going but be careful...")
    elif numberoflives == 1:
        print("You're on your last life. You only have Sugar left... be very careful be very strong", name, "!")
  
#initialize space to 0
space = 0

#24 spaces is end of the game
while space < 24:
    #ask the user if they would like to roll the dice and validate input
    play = input("Would you like to roll the dice? Enter 'y' or 'n'. ")
    while play not in {'y', 'n'}:
        play = input("Try again! ")
    #set rollValue to the value set by the function, inside the loop so it keeps changing
    rollValue = diceRoll(play)
    #set space to accumulate each rollValue to move through the game
    space = space + rollValue 
    if space == 1:
        print("You landed on space 1") #FILL IN THE BLANKS HERE
        
    elif space == 2:
        print("Elmer, your classmate at Pokey Oaks Kindergarten, is eating paste and all the kids are teasing him. Buttercup even throws a ball of paste at his face! \n He gets cleaned up and sent outside to play by the teacher, but he sits under a tree with his jar of paste.")
        print("Meanwhile, a fly inside a garbage truck eats off a napkin from a nearby Marshmallow Toxic Filter Site and becomes radioactive!")
        print("The garbage truck drives by Pokey Oaks and the fly ends up in Elmer's paste. Elmer accidentally eats it and becomes a giant monster, made of glue!!!")
        print("...")
        print("He is tearing up the town, and everything is sticking to him!")
        decision2 = input("What should we do? \n Enter 1 to Fight! \n Enter 2 to apologize. ")
        while decision2 not in {'1', '2'}:
            decision2 = input("Enter 1 to Fight or 2 to apologize. ")
        if decision2 == "1":
            print("You get stuck in Elmer's glue. Fighting won't solve all of your problems! You lose one life.")
            numberoflives -= 1
        elif decision2 == "2":
            print("Elmer accepts your apology! You saved the town and don't lose any lives!")
    
    elif space == 3:
        print("You landed on space 3") #FILL IN THE BLANKS HERE   
    elif space == 4:
        print("You landed on space 4") #FILL IN THE BLANKS HERE
    elif space == 5:
        print("You landed on space 5") #FILL IN THE BLANKS HERE
    elif space == 6:
        print("You landed on space 6") #FILL IN THE BLANKS HERE
        
    elif space == 7:
        print("MOJO JOJO has sprayed you with his mind-warping banana ray gun.. MOJO JOJO! ...I have you now, ", name, "!")
        numberoflives -= 1
        print(numberoflives)
        decision7 = input("Do you want revenge on MOJO JOJO?! Should you get up and spray him with your pixie stick gun? ")
        while decision7 not in {"Y","y","yes","Yes","N","n","No","no"}:
            input("Not a correct response, Do you want or revenge on MOJO JOJO or not!?!!!")
        if decision7 in {"Y", "y", "Yes", "yes"}:
            numberoflives-= 1
            print("You are too weak to retaliate and therefore lose another life. MOJO JOJO rejoices, \"You foolish girl! You cannot beat my ray gun MUHAHAHAH\"")
        elif decision7 in {"N", "n", "No", "no"}: 
            print("You have evaded a potential serious attack from MOJO JOJO, and have fled just losing that one life")
    
    elif space == 8:
        decision8 = input("You've run into a magic potion. Pink, bubbly, and shiny... do you want to drink it? " )
        while decision8 not in {"Y","y","yes","Yes","N","n","No","no"}:
            input("Not correct response, Do you want to drink the pink magic potion or not? Quit fooling around by pressing other keys. ")
        if decision8 in {"Y", "y", "Yes", "yes"}:
            numberoflives -= 1
            print("The magic potion has a negative effect! It hurts you and you start throwing up nothing but sweet candy: you lose a life ", name, ".")
            print(numberoflives)
            diceRoll(play)
        if decision8 in {"N", "n", "No", "no"}:
            print("The potion was bad news", name, "!!")

    elif space == 9:
        print("You have encountered Professor Utonium and take a moment to clear your mind. You tell him about the struggle of dealing with all the villains. And y'all have some pink tea.")       
                        
    elif space == 10:
        decision10 = input("You trespass in Fuzzy Lumpkins property while traveling through the woods. He gets really angry and turns blood-red and is ready to attack you. Do you try to calm him down and say \"OOOO SAAA\" Y or N? ")
        while decision10 not in {"Y","y","yes","Yes","N","n","No","no"}:
            input("Not correct response, Do you want to soothe him by saying \"OOOO SAAAA\" Yes or No? ")
        if decision10 in {"Y", "y", "Yes", "yes"}:
            print("Great decision. Fuzzy Lumpkins is dangerous when he is angry and could've caused serious damage to you. He has calmed down and offered you another dice roll. POWERPUFF GO!")
            diceRoll(play)
        if decision10 in {"N", "n", "No", "no"}:
            numberoflives -= 1
            print("Fuzzy Lumpkins gets even more angry and throws you against the floor. You're seriously hurt and lose a life. You flee and get away while Fuzzy chases you but he's not fast enough to keep up.")

    elif space == 11:
        print("You have landed in the land of Sugar Spice and everything nice; you receive an extra life and an extra dice roll. Life couldn't be better for a Powerpuff girl!")
        if numberoflives < 4:
            numberoflives += 1
        else:
            print("Well, you already have four, you couldn't possibly handle any more lives...") 
    
    elif space == 12:
        print("You have encountered the Gangreen Gang and the Grubber does a supersonic burp that leaves you dazed. You faint from the stink and lose a life.")
        numberoflives -= 1
        
    elif space == 13:
        print("You landed on space 13")    #FILL IN THE BLANKS HERE
    elif space == 14:
        print("You landed on space 14")    #FILL IN THE BLANKS HERE
    elif space == 15:
        print("You landed on space 15")    #FILL IN THE BLANKS HERE
    elif space == 16:
        print("You landed on space 16")    #FILL IN THE BLANKS HERE
    elif space == 17:
        print("You landed on space 17")    #FILL IN THE BLANKS HERE
    elif space == 18:
        print("You landed on space 18")    #FILL IN THE BLANKS HERE
    elif space == 19:
        print("You landed on space 19")    #FILL IN THE BLANKS HERE
    elif space == 20:
        print("You landed on space 20")    #FILL IN THE BLANKS HERE
    elif space == 21:
        print("You landed on space 21")    #FILL IN THE BLANKS HERE
    elif space == 22:
        print("You landed on space 22")    #FILL IN THE BLANKS HERE
    elif space == 23:
        print("You landed on space 23")    #FILL IN THE BLANKS HERE
    elif space == 24:
        print("You landed on space 24")    #FILL IN THE BLANKS HERE
    lives()
print("end of game message")