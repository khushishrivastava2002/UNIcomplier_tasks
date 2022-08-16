"""
  Number guessing game 
                
            It is a simple game of number guessing in this the computer will generate any number between 1 to 50, and you have to 
            guess the number between the range 1 to 50, 
            
            Every time whenever you guess wrong the computer will gives us a hint that either the number that you have entered is low or high so you have to 
            chosse according in next chance.
            Only 5 chances are given to guess correctly.
    """


import random
number = random.randint(1 , 50)
guess = int(input("Enter your guess number between 1 to 50: "))
chance = 0 
if number == guess:
    print("congo!")
else:
     while chance<5:
        if guess<number:
            print("WRONG ANS!! ")
            print("HINT: Your guess is low")
            guess = int(input("enter an interger from 1 to 50:- "))    
        else:
            print("WRONG ANS!! ")
            print("HINT: your guess is high")
            guess = int(input("enter an interger from 1 to 50:- "))
        chance = chance + 1
print("The correct ans is: -",number)        
