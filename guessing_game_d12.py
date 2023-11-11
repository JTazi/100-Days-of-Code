# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:55:16 2023

@author: john tazioli
"""
#guessing game
#computer picks number between 1-100, user guesses within 5 or10 guesses to win

import random as r


def guessing_game():
    print("Guessing Game!")
    mode = input("Would you like to play  hard or easy mode? ('h'/'e')\n")
    goal = r.randint(1,100)
    
    if mode == 'h':
        num_guess = 5
    else:
        num_guess = 10
    
    while  num_guess > 0:
        print(f'{num_guess} Guesses Remaining.')
        guess = int(input("Guess a number between 1-100:"))
        if guess > goal:
            print(f"Wrong, the number is less than {guess}.")
        elif guess < goal:
            print(f"Wrong, the number is greater than {guess}.")
        elif guess  == goal:
            print(f"Right, you win! The number is {guess}")
            return
        num_guess -= 1
    
    print("No more guesses, you lose.")
    return


#improvements
#input checking to ensure user inputs proper things
#dummy proof guessing, ensure user only guesses within the available  possible answers