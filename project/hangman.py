# intro
print("Hello Gamer! What is your good name?")
name = input()
print("Hi " +name+ "!")
print("******HERE ARE SOME RULES******")
print("----------------------------------------------------------------")
print("Use only lowercase letters!")
print("You've got 6 lives and each incorrect answer will cost a body part!!")
print("Once all the 6 lives are used, the man will be hanged!!!")
print("----------------------------------------------------------------")
print("~Lets start The Hangman Game~")
print("Save the man with your luck,fight for it!")
print("----------------------------------------------------------------")

#words
import random
from words import words
word = random.choice(words)

#game begins
guesses=''
lives=6
while lives>0:
    wrong = 0

    for letter in word:
        if letter in guesses:
            print(char)    
        else:
            print("_") 
            wrong +=1
        
    if wrong==0:
        print("YOU WON!!!")
        print("The word is : ",word)
        break
    guess=input("Guess a word:")

    guesses+= guess
    if guess not in word:
        lives -=1
        #To Draw hangman
        if lives == 6:
            print("+------------+")
            print("|            |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("+-------+")
            print("RIGHT GUESS")
            print("You have only 6 lives left")
           
        elif lives == 5:
            print("+------------+")
            print("|            |")
            print("|            O")
            print("|")
            print("|")
            print("|")
            print("|")
            print("+-------+")
            print("WRONG GUESS")
            print("You have only 5 lives left")
           
        elif lives == 4:
            print("+------------+")
            print("|            |")
            print("|            O")
            print("|            |")
            print("|")
            print("|")
            print("|")
            print("+-------+")
            print("WRONG GUESS")
            print("You have only 4 lives left")
            
        elif lives == 3:
            print("+------------+")
            print("|            |")
            print("|            O")
            print("|            |")
            print("|           /")
            print("|")
            print("|")
            print("+-------+")
            print("WRONG GUESS")
            print("You have only 3 lives left")
            
        elif lives == 2:
            print("+------------+")
            print("|            |")
            print("|            O")
            print("|            |")
            print("|           / \\")
            print("|")
            print("|")
            print("+-------+")
            print("WRONG GUESS")
            print("You have only 2 lives left")
            
        elif lives == 1:
            print("+------------+")
            print("|            |")
            print("|            O")
            print("|            |\\")
            print("|           / \\")
            print("|")
            print("|")
            print("+-------+")
            print("WRONG GUESS")
            print("You have only 1 life left")
            
        elif lives == 0:
            print("+------------+")
            print("|            |")
            print("|            O")
            print("|           /|\\")
            print("|           / \\")
            print("|")
            print("|")
            print("+-------+")
            print("GAME OVER")
            print("The correct word is:",word)



