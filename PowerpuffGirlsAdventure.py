# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:22:41 2019

@author: Cortney, Dennis, Thuy, and Christopher

Please change your Spyder Theme to a DARK THEME!
"""

import random
from colorama import Fore, Style

#This function rolls the dice and validates input     
def diceRoll(play):
    min = 1
    max = 3
    if play == "y":
        rollValue = random.randint(min, max)
        print("...\n...\n....\n.....\nYou rolled", rollValue, "!\n")
    elif play == "n":
        print("Okay, Game over!")
    return rollValue

#define function that lets the user know how they are doing
def lives():
    if numberoflives == 0:
        #insert a function here to end game and ask if they want to play again?
        print(Fore.GREEN + "\nGame over!!", name, "and the rest of the Powerpuff Girls are no more, MOJO JOJO! >:(")
    elif numberoflives == 4:
        print(Fore.GREEN + "\nSugar, Spice, Everything Nice, and Chemical X... You have all 4 lives. You go girl!")
    elif numberoflives == 3:
        print(Fore.GREEN + "\nYou have got three lives", name,": Sugar, Spice, and everything nice. Chemical X is missing and ahhhh your powers are getting weaker...")
    elif numberoflives == 2:
        print(Fore.GREEN + "\nYou have got two lives", name,": Sugar and Spice, keep going but be careful...")
    elif numberoflives == 1:
        print(Fore.GREEN + "\nYou're on your last life. You only have Sugar left... be very careful be very strong", name, "!")
        
playAgain = 'Y'
while playAgain in ['yes', 'YES', 'Yes', 'y', 'Y']:
    #initialize space to 0
    space = 0
    print(Fore.CYAN + Style.BRIGHT + "**********\nSugar, spice, and everything nice... These were the ingredients chosen to create the perfect little girls.\nBut Professor Utonium accidentally added an extra ingredient to the concoction-- Chemical X. \nThus, The Powerpuff Girls were born! Using their ultra-super powers: Blossom, Bubbles, and Buttercup have dedicated their lives to fighting crime and the forces of evil!!")   
    #print the basic objectives of game
    print("THE CITY OF TOWNSVILLE!\nNeeds your help! Navigate through Mojo Jojo's lair and even Pokey Oaks Kindergarten by rolling the dice, saving the town and making smart decisions along the way! Make it through all 24 spaces with at least one life and you have beaten the game. POWERPUFF GO!")
    #Ask the user which Powerpuff girl they would like to be, and validate input     
    name = input(Fore.WHITE + "Which Powerpuff girl do you want to be? Bubbles, Buttercup, or Blossom? ")
    while name not in {'Buttercup','buttercup','BUTTERCUP',"Bubbles",'bubbles','BUBBLES','Blossom','blossom','BLOSSOM'}:
        name = input("Not an eligible player... which Powerpuff girl do you want to be? \n Bubbles, Buttercup, or Blossom? ")

    #Set initial lives to 4        
    numberoflives = 4

    #24 spaces is end of the game
    while (space < 24):
        #ask the user if they would like to roll the dice and validate input
        play = input(Fore.WHITE + "Enter 'y' to roll the dice: ")
        while play not in {'y', 'Y'}:
            play = input("Try again! ")
        #set rollValue to the value set by the function, inside the loop so it keeps changing
        rollValue = diceRoll(play)
        #set space to accumulate each rollValue to move through the game
        space = space + rollValue
        #set up a few 
        if space in {3,5,7,9,11,15,17,19,21}:
            print(Fore.MAGENTA + "You are on space number", space, ". Keep going!")
            
        if space == 1:
            print(Fore.BLUE + "Just getting started and", name, "is already taking a break? This is only space number one, keep going! <3")
        
        elif space == 2:
            print(Fore.MAGENTA + "Elmer, your classmate at Pokey Oaks Kindergarten, is eating paste and all the kids are teasing him. You even throw a ball of paste at his face! \nHe gets cleaned up and sent outside to play by the teacher, but he sits under a tree with his jar of paste.")
            print(Fore.MAGENTA + "Meanwhile, a fly inside a garbage truck eats off of a napkin from a nearby Marshmallow Toxic Filtration Site and becomes radioactive!")
            print(Fore.MAGENTA + "The garbage truck drives by Pokey Oaks and the fly ends up in Elmer's paste. Elmer accidentally eats it and becomes a giant monster, made of glue!!!")
            print(Fore.MAGENTA + "...")
            print(Fore.MAGENTA + "He is tearing up the town, and everything is sticking to him!")
            decision2 = input(Fore.WHITE + "What should we do? \n Enter 1 to Fight! \n Enter 2 to apologize for throwing the ball of paste. ")
            while decision2 not in ['1', '2']:
                decision2 = input("Enter 1 to Fight or 2 to apologize. ")
            if decision2 == "1":
                print(Fore.MAGENTA + "\nYou get stuck in Elmer's glue. Fighting won't solve all of your problems! You lose one life.")
                numberoflives -= 1
            elif decision2 == "2":
                print(Fore.MAGENTA + "\nElmer accepts your apology! You saved the town and don't lose any lives!")
    
        elif space == 3:
            print(Fore.CYAN + "Meanwhile, in Townsville Jail, Mojo Jojo is flushing armpit hair, snails from the prison cafeteria, and the tail of a talking dog down the jail cell toilet. What is he making???")
            print(Fore.CYAN + "It's the Rowdyruff Boys! The concoction created 3 superpowered boys, one for each of the Powerpuff Girls!")
            if name in ['blossom','Blossom','BLOSSOM']:
                rowdyName = "Brick"
                print(name,", you are fighting", rowdyName, "!")
            elif name in ['bubbles','Bubbles','BUBBLES']:
                rowdyName = "Boomer"
                print(name,", you are fighting", rowdyName, "!")
            elif name in ['buttercup','Buttercup','BUTTERCUP']:
                rowdyName = "Butch"
                print(Fore.CYAN + name,", you are fighting", rowdyName, "!")
            print(Fore.CYAN + "They are pretty tough, we have to think outside the box to beat them!")
            decision3 = input(Fore.WHITE + "What do little boys fear most in the world? \n Enter 1 for 'slimy bugs' \n Enter 2 for 'massive punches to the face' \n Enter 3 for 'cooties' \n ...")
            while decision3 not in ['1','2','3']:
                decision3 = input("Don't be silly! Enter 1, 2, or 3!" )
            if decision3 == "1":
                print("These boys are made of part snail! Haven't you been paying attention?? You get punched back a space by", rowdyName, "!")
                space -= 3
                print("You are on space", space, ".")
            elif decision3 == "2":
                print("These are the ROWDYRUFF BOYS. THEY ARE HERE TO FIGHT!", rowdyName, "punched a life out of you.")
                numberoflives -= 1
            elif decision3 == "3":
                print("Boys hate cooties! You kissed", rowdyName, "and he exploded! Take this extra life with you!")
                numberoflives += 1
        
        elif space == 4:
            print(Fore.YELLOW + "You had a super boost of speed! Jump ahead 3 spaces!")
            space += 3
        
        elif space == 5:
            print(Fore.GREEN + "The Powerpuff Girls are growing girls, Professor Utonium is urging you to eat your broccoli!")
            decision5 = input( Fore.WHITE + "Eat some broccoli? y/n ")
            while decision5 not in {"Y","y","yes","Yes","N","n","No","no"}:
                decision5 = input("Eat your veggies?")
            print(Fore.GREEN + "Broccoli Aliens have invaded the Earth after infecting all the parents of Townsville with alien mind control spores. None of the children of Townsville ate their vegetables!")
            if decision5 in {"Y", "y", "Yes", "yes"}:
                print("Except you! You ate infected broccoli, which sent you back 1 space while the rest of the Powerpuff Girls and Townsville's youth save the day.")
                space -= 1
            elif decision5 in {"N", "n", "No", "no"}:
                print(Fore.GREEN + "Now it is up to the kids to save the day! You remember what the Professor said... \n'The only way to get rid of all your broccoli is to eat it all up.'")
                print(Fore.GREEN + "'We gotta eat 'em to beat 'em!', you say to the rest of the girls!")
            
        elif space == 6:
            print(Fore.RED + "No fighting for the Powerpuff Girls today, they are all sick!")
        
        elif space == 7:
            print(Fore.MAGENTA + "MOJO JOJO has sprayed you with his mind-warping banana ray gun... MOJO JOJO! ...I have you now,", name, "!")
            numberoflives -= 1
            decision7 = input(Fore.WHITE + "Do you want revenge on MOJO JOJO?! Should you get up and spray him with your pixie stick gun? ")
            while decision7 not in {"Y","y","yes","Yes","N","n","No","no"}:
                input("Not a correct response, Do you want or revenge on MOJO JOJO or not!?!!!")
            if decision7 in {"Y", "y", "Yes", "yes"}:
                numberoflives-= 1
                print("You are too weak to retaliate and therefore lose another life. MOJO JOJO rejoices, \"You foolish girl! You cannot beat my ray gun MUHAHAHAH\"")
            elif decision7 in {"N", "n", "No", "no"}: 
                print("You have evaded a potential serious attack from MOJO JOJO, and have fled just losing that one life")
    
        elif space == 8:
            print(Fore.MAGENTA + "You've run into a magic potion. Pink, bubbly, and shiny..." )
            decision8 = input(Fore.WHITE + "do you want to drink it? " )
            while decision8 not in {"Y","y","yes","Yes","YES","N","n","No","no","NO"}:
                input("Not correct response, Do you want to drink the pink magic potion or not? Quit fooling around by pressing other keys. ")
            if decision8 in {"Y", "y", "Yes", "yes"}:
                numberoflives -= 1
                print("The magic potion has a negative effect! It hurts you and you start throwing up nothing but sweet candy: you lose a life", name, ".")
            elif decision8 in {"N", "n", "No", "no"}:
                print("That potion was bad news", name, "!! Stay vigilant!")

        elif space == 9:
            print(Fore.BLUE + "You have encountered Professor Utonium and take a moment to clear your mind. You tell him about the struggle of dealing with all the villains. And y'all have some pink tea.")       
                        
        elif space == 10:
            print(Fore.BLUE + "You trespass in Fuzzy Lumpkins property while traveling through the woods. He gets really angry and turns blood-red and is ready to attack you.")
            decision10 = input(Fore.WHITE + "Do you try to calm him down and say \"OOOO SAAA\" Y or N? ")
            while decision10 not in {"Y","y","yes","Yes","N","n","No","no"}:
                input("Not correct response, Do you want to soothe him by saying \"OOOO SAAAA\" Yes or No? ")
            if decision10 in {"Y", "y", "Yes", "yes"}:
                print(Fore.BLUE + "Great decision. Fuzzy Lumpkins is dangerous when he is angry and could've caused serious damage to you. He has calmed down and offered you another dice roll. POWERPUFF GO!")
            elif decision10 in {"N", "n", "No", "no"}:
                numberoflives -= 1
                print(Fore.BLUE + "Fuzzy Lumpkins gets even more angry and throws you against the floor. You're seriously hurt and lose a life. You flee and get away while Fuzzy chases you but he's not fast enough to keep up.")

        elif space == 11:
            print(Fore.GREEN + "You have landed in the land of Sugar Spice and everything nice; you receive an extra life and an extra dice roll. Life couldn't be better for a Powerpuff girl!")
            if numberoflives < 4:
                numberoflives += 1
            else:
                print("Well actually, you already have four lives, you couldn't possibly handle any more...") 
    
        elif space == 12:
            print(Fore.GREEN + "You have encountered the Gangreen Gang and the Grubber does a supersonic burp that leaves you dazed. You faint from the stink and lose a life.")
            numberoflives -= 1
        
        elif space == 13:
            print(Fore.MAGENTA + "You have landed on unlucky space 13... Kablooey! You lose a life.")
            numberoflives -= 1

        elif space == 14:
            print(Fore.CYAN + "You have landed at the Powerpuff Girls Headquarters (really your bedroom) \nprepare for a power-up (a much needed nap) \nYou receive an extra life. Life couldn't be better for a Powerpuff girl!")
            if numberoflives < 4:
                numberoflives += 1
            else:
                print("Well, you already have four, you couldn't possibly handle any more lives...") 

        elif space == 15:
            print(Fore.BLUE + "You have landed at Pokey Oaks Kindergarten. Spend some time in the library to strategize on a way to defeat Mojo Jojo!")       

        elif space == 16:
            decision16 = input(Fore.GREEN + "You are sneaking into Mojo Jojo's hideout. He could be hiding. Do you try to find him and take him down\" Y or N? ")
            while decision16 not in {"Y","y","yes","Yes","N","n","No","no"}:
                input("Not correct response, Do you want to take him down, Yes or No? ")
            if decision16 in {"Y", "y", "Yes", "yes"}:
                print("Great decision. MOJO JOJO plans to destroy the Powerpuff girls. However he has left the hideout but left plans for his next attack, so time for another dice roll. POWERPUFF GO!")
            if decision16 in {"N", "n", "No", "no"}:
                numberoflives -= 1
                print("Although Mojo Jojo has left his hideout, the PowerPuff Girls lose a life.")

        elif space == 17:
            decision17 = input(Fore.CYAN + "You have been called to the Mayor's Office to brief about Mojo Jojo's plan to build an Ultimate Townsville Destruction Device do you go? Y or N? ")
            while decision17 not in {"Y","y","yes","Yes","N","n","No","no"}:
                input("Not correct response, Do you go to the Mayor's office, Yes or No? ")
            if decision17 in {"Y", "y", "Yes", "yes"}:
                print(Fore.CYAN + "Great decision. The mayor appoints you CITY DEFENDER and gives you the key to the town. Time to hunt down Mojo Jojo, get going!")
            if decision17 in {"N", "n", "No", "no"}:
                numberoflives -= 1
                print("The mayor labels you town enemy number one and suspects you of conspiring against the town. He takes a life.")

        elif space == 18:
            decision18 = input(Fore.MAGENTA + "Mojo is preparing his destruction device. Do you try to find him and take him down Y or N? ")
            while decision18 not in {"Y","y","yes","Yes","N","n","No","no"}:
                input("Not correct response, Do you want to take him down \ Yes or No? ")
            if decision18 in {"Y", "y", "Yes", "yes"}:
                print("Great decision. MOJO JOJO's weapon is designed to destroy the Powerpuff girls and you have thwarted him this time. POWERPUFF GO!")
            if decision18 in {"N", "n", "No", "no"}:
                numberoflives -= 1
                print("... The Powerpuff Girls never miss a chance to take down Mojo Jojo! Come on,", name, "try harder next time!")
   
        elif space == 19:
            print(Fore.RED + "A fashion-related vandal is going around Townsville. After the “trashy” look gets replaced with the “dull” look, a mysterious villain named Mask Scare awakens.\n She gives the people of Townsville bad makeovers that are seemingly impossible to remove.")  
            print(Fore.RED + "If you are", name, "\n     *How lucky you are* \n          Because you are the first human victim of Mask Scare.")
            decision19 = input(Fore.WHITE + "How do you want to deal with it? \n Enter 1 to Leave the makeup on. \n Enter 2 to Find a way to remove it ASAP. ")
            while decision19 not in {'1', '2'}:  
                decision19 = input("Enter 1 to Leave it as it is or 2 to Need to take it off ASAP no matter what. ")             
            if decision19 == "1":
                print(Fore.RED + "You are confident in your beauty. Your goal is to focus on trying to find Mask Scare to strike her down.\n Bravo,",name,"! Your current life is fully protected.")   
            elif decision19 == "2":
                print(Fore.RED + "Okay. It's so annoying to have something on your face and the other two Powerpuffs try to remove the makeup for you...\nOops, unfortunately, unsuccessful mission. You got allergic to the powder used by Mask Scare.\n You cannot suffer through the pain. I'm sorry. \n Better luck next try.")  
                numberoflives -= 1                 
    
        elif space == 20:
            print(Fore.GREEN + "It is the day before Christmas Eve in Townsville. And Santa wants to send a present early by announcing there's a new Powerpuff Girl in town....")
            decision20 = input(Fore.WHITE + "Are you excited? ")
            while decision20 not in {"Y","y","yes","Yes","N","n","No","no"}:
                decision20 = input("I don't get what you mean. Are you excited or not?")
            if decision20 in {"Y", "y", "Yes", "yes"}:
                numberoflives -= 1
                print("You are in a fiendishly foul plot. Now, you must explode into a Yuletide tornado of bad-girl-thwarting action to trick Santa from not turning Princess (your spoiled, non-superpowered classmate) into the fourth Powerpuff Girl!! She kicks your butt at least once though...")
            elif decision20 in {"N", "n", "No", "no"}:
                numberoflives += 1
                print("Wohohh!! You avoided a fiendishly foul trap.\n You gain one more life to keep Christmas from disappearing.")
             
        elif space == 21:
            print(Fore.CYAN + "You have landed on a race for a mysterious chest that was held by the Mayor. And all of Townsville's villains join in to win it.\n But you enter to keep them from doing so...\nNaturally, things escalate quickly. You cannot protect your lives.")
            numberoflives -= 1
    
        elif space == 22:
            print(Fore.BLUE + "All of the villains of Townsville break free from prison to search for a key. Not any ordinary key... \nthat's the key to rule the world!!! \nYou must find the key and return it to the Mayor, before the villains get to it.")
            decision22 = input(Fore.WHITE + "What do you want to do? \nEnter 1 if you want to beat all of the villains, then find the key later or \nEnter 2 to decide the most important is find the key and decide on ideas for ruling the world. ")
            while decision22 not in {'1', '2'}:  
                decision22 = input("Enter 1 to Beat or 2 to Join in the race")
            if decision22 == "1":
                decision22 = input("You cannot beat all the villains at once. You are beaten so painfully... till your new life starts")  
                numberoflives -= 1
            elif decision22 == "2":
                print("You have no luck until Mojo Jojo points out that the Mayor is a complete idiot and probably left the key in his desk.\nYou found it.\nYou get one more life to decide on how you want to rule this world.")  
                numberoflives += 1               
    
        elif space == 23:
            print(Fore.RED + "I'm so sorry to inform you that the Professor turned you and everyone else in Townsville into babies and you lost your superpowers.\n Good job! You've made it this far but sorry, you cannot make it until the end!!\n Wish you a better luck next time!")
            #Set variables to quit from dice roll and print game over message
            space = 25
            numberoflives = 0
            
        #call the lives function to print a message letting the user know how they are doing
        if numberoflives == 0:
            space = 25
        if space == 24:
            print(Fore.GREEN + "Congratulations!! You've made it with", numberoflives, "remaining. Now it is time for enjoying Christmas holidays with the other two Powerpuff girls.")
        lives()  

    #ask the user if they want to play again      
    playAgain = input(Fore.WHITE + "**********\nThank you for enjoying our game. Would you like to play again? Y/N: ")