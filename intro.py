# intro
print("Hello Gamer! What is your good name?")
name = input()
print("Hi " +name+ "!")
print("******HERE ARE SOME RULES******")
print("----------------------------------------------------------------")
print("You've got 6 lives and each incorrect answer will cost a body part!!! ")
print("Once all the 6 lives are used, the man will be hanged!!!")
print("----------------------------------------------------------------")
print("~Lets start The Hangman Game~")
print("Save the man with your luck,fight for it!")
print("----------------------------------------------------------------")

#words
import random

from words import words

print("The random word is " +random.choice(words))
