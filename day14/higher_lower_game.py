# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:38:57 2023

@author: jtazioli

main file for a higher or lower game.
present user with two instagram accounts, ask them to guess if a has higher or lower like count  than b
if user guesses right, continue to new round, track score.
"""
#import dependencies
import inputs.game_data as gd
import random as r

#establish globals
data = gd.data
lose = False
win_count = 0

#def functions

def  pick_names():
    #use random library to pick 2 random entries from data list
    #ensure the same entry isn't picked twice
    #return the indexes of the 2 entries
    name1 = r.randint(0,9)
    name2 = r.randint(0,9)
    while name2 == name1:
        name2 = r.randint(0,9)
    return name1,name2

def get_guess():
    #que user for input, check for validity and re-request input if invalid
    #return 'h' or 'l' guess
    approved = ['h','l']
    g = input("Higher or Lower? ('h' / 'l')")
    while g not in approved:
        g = input("Incorrect input, 'h'igher or 'l'ower?")
    return g

def get_ans(l1,l2):
    #take in number of likes from data and return if the right answer is 'h' or 'l'
    if l1 > l2:
        return 'h'
    else:
        return 'l'

#game title
print("Higher or Lower!")

#main game loop
while lose == False:
    #get 2 entries from data
    n1,n2 = pick_names()
    print(f"Name: {data[n1]['name']}, {data[n1]['desc']} from {data[n1]['country']}.")
    print("OR")
    print(f"Name: {data[n2]['name']}, {data[n2]['desc']} from {data[n2]['country']}.")
    
    #get user guess
    guess = get_guess()
    
    #compute right answer
    ans = get_ans(data[n1]['likes'],data[n2]['likes'])
    
    #test if user is right and proceed accordingly
    if guess == ans:
        win_count += 1
        print(f"Correct! You've made it {win_count} rounds.")
    else:
        lose = True
        print(f'Wrong, you made it {win_count} rounds.')
        