# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:04:29 2023

@author: jtazioli
"""

import random as r
from resources import deck
from resources import card_value

def hand_value(hand_lst):
    val = 0
    for card in hand_lst:
        if card[0] == 'A' and (val + 11) <= 21:
            val+= card_value[card[0]][1]
        elif card[0] == 'A' and (val + 11) > 21:
            val+= card_value[card[0]][0]
        else:
            val += card_value[card[0]]
    
    if val >21 and ('AH' in hand_lst or 'AD' in hand_lst or 'AS' in hand_lst or 'AC' in hand_lst):
        val -= 10
    
    return val

def hit(hand):
    hand.append(deck.pop(r.randint(0,len(deck)-1)))
    print(hand)
    if hand_value(hand) > 21:
        print("BUST!")
        return hand
    else:
        choice = input('Hit (h) or stand (s)? ')
        if choice == 'h':
            hit()
        else:
            return hand

def blackjack():
    print("BLACKJACK")
    play_game = True
    
    
    #while play_game == True:
        
        
        
def single_hand():
    player_hand  = [deck.pop(r.randint(0,len(deck)-1)),
                    deck.pop(r.randint(0,len(deck)-1))]
    dealer_hand = [deck.pop(r.randint(0,len(deck)-1)),
                    deck.pop(r.randint(0,len(deck)-1))]
    
    options = {'s':'stand','h':'hit','d':'double','sp':'split','sur':'surrender'}
    
    player_turn = True
    #dealer_turn = True
    game_over = False
    
    while game_over == False:
            
        while player_turn == True:
            decision = input(f"Your Hand: {player_hand}\nWhat do you want to do? {options}")
            
            if decision == 's':
                player_turn = False
            elif decision == 'h':
                while hand_value(player_hand) <= 21 and decision == 'h':
                    player_hand = hit(player_hand)
                    decision = input(f"You're hand is: {player_hand}\n 'h'it or 's'tand? ")
                if hand_value(player_hand) > 21:
                    game_over = True
                    player_turn = False
                else: 
                    player_turn = False
        
        player_val = hand_value(player_hand)
    
        while hand_value(dealer_hand) < player_val:
            
            if hand_value(dealer_hand) < 17:
                dealer_hand = hit(dealer_hand)
            else:
                dealer_turn = False
                game_over = True
        dealer_turn = False
        game_over = True
    
    dealer_val = hand_value(dealer_hand)
            
    if dealer_val > 21
                
       # elif decision == 'd':
        
        #elif decision == 'sp':
            
        #elif decision == 'sur':