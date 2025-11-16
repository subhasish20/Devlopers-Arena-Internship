# Build a number guessing game using if-else statements

import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the right number.")

number_guessing_game()
