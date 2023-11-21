# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:09:20 2023

@author: jtazioli

Hangman main
"""

import random as r

import hm_res as hm
from hm_res import stages
from hm_res import logo


def hangman():
    game_on = True
    word = hm.pick_word()
    display = '_'
    guessed = []
    lives = 6
    
    for x in range(1,len(word)):
        display += " _"
    
    print(logo)
    
    while game_on:
        print('-----------------\n')
        print(display)
        guess = hm.get_guess(guessed)
        guessed.append(guess)
        
        if guess not in word:
            lives -= 1
            print(f'{guess} is not in the word!')
            print(stages[lives])
        
        elif guess in word:
            loc = word.find(guess)
            while loc != -1:
                temp = display.split(' ')
                temp[loc] = guess
                display = ' '.join(temp)
                loc = word.find(guess,loc+1)
            print('Good Guess!')
            
        if lives == 0:
            print('GAME OVER! You Lose.')
            game_on = False
            
        elif "_" not in display:
            print(f'You win, the word is: {word}')
            game_on = False


        
        
    

        