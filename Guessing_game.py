# GUESS A NUMBER GAME

import random

number = random.randint(1, 100)

print(" Number Guessing Game")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Guessed lower number! Try again.")
    elif guess > number:
        print("Guessed higher number! Try again.")
    else:
        print("YAYYYY...! You guessed the number Correctly!")
        break