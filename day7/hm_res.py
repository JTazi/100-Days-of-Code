# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:09:21 2023

@author: jtazioli

Hangman Resources
"""

import random as r

def pick_word():
    #pick word from list of words and return the word as string and list of characters in word
    #requires random package
    word_list = ['zero','one','two','three','four','five']
    word = word_list[r.randint(0,len(word_list)-1)]
    print(word)
    return word

def get_guess(guessed):
    guess_check = True
    letter = input(f"Already Guessed: {guessed}\nWhat letter do you want to guess?\n").lower()
    while guess_check:
        if letter in guessed:
            letter = input("Already guessed that, guess again!").lower()
        elif len(letter) != 1:
            letter = input("More than one character entered, try again.").lower()
        else:
            guess_check = False
            
    return letter

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                     