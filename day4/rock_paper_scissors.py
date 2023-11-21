# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:35:40 2023
Future Work: add play again feature with score tracker
@author: jtazioli
"""
import random

#function to check  user input 
def check(inp,approved_inps):
    if inp in approved_inps:
        return True
    else:
        return False

#rock,paper,scissors. user provides input, RNG picks for computer, outcome displayed
def rps():
    #outcome table for player, then pc picks
    rps_logic = {'r':{'r':'draw','p':'lose','s':'win'},
                 'p':{'r':'win','p':'draw','s':'lose'},
                 's':{'r':'lose','p':'win','s':'draw'}}
    
    pc_converter = ['r','p','s']
    acronym_converter = {'r':'rock','p':'paper','s':'scissors'}
    
    user_pick = input("Welcome to rock, paper, scissors. Enter your choice as 'r','p', or 's':\n")
    while check(user_pick, pc_converter)==False:
        user_pick = input("Invalid  Selection, try again. Enter your choice as 'r','p', or 's':\n")
    rand_int = random.randint(0,2)
    comp_pick = pc_converter[rand_int]
    
    outcome = rps_logic[user_pick][comp_pick]
    print(f'You played {acronym_converter[user_pick]}, computer played {acronym_converter[comp_pick]}. You {outcome}!')
    return