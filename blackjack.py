# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 10:22:02 2023

@author: tazma
"""
import random as r


def hit(deck):
    #input cards left in deck, output 1 card and deck without that card
    r.randint(0,len(deck)-1)
    return deck.pop(r.randint(0,len(deck)-1)),deck

def hand_value(hand):
    val_dict = {'AH':11,'2H':2,'3H':3,'4H':4,'5H':5,'6H':6,'7H':7,'8H':8,'9H':9,'10H':10,'JH':10,'QH':10,'KH':10,
            'AC':11,'2C':2,'3C':3,'4C':4,'5C':5,'6C':6,'7C':7,'8C':8,'9C':9,'10C':10,'JC':10,'QC':10,'KC':10,
            'AD':11,'2D':2,'3D':3,'4D':4,'5D':5,'6D':6,'7D':7,'8D':8,'9D':9,'10D':10,'JD':10,'QD':10,'KD':10,
            'AS':11,'2S':2,'3S':3,'4S':4,'5S':5,'6S':6,'7S':7,'8S':8,'9S':9,'10S':10,'JS':10,'QS':10,'KS':10}
    val = 0
    for card in hand:
        val += val_dict[card]
        
    if val > 21 and 'AH' in hand or 'AC' in hand or 'AD' in hand or 'AS':
        val -= 10
    
    return val


def blackjack():
    deck = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
            'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
            'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
            'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC']
    p_hand = []
    d_hand = []
    
    if input("Would you like to play blackjack? (y/n)\n") == 'y':
        card,deck = hit(deck)
        p_hand.append(card)
        card,deck = hit(deck)
        p_hand.append(card)
        
        card,deck = hit(deck)
        d_hand.append(card)
        card,deck = hit(deck)
        d_hand.append(card)
        
        p_turn = True
        
        while p_turn == True:
            p_dec = input(f'You have: {p_hand}\nDealer has:{d_hand[0]}\n(h)it or (s)tand? ')
            
            if p_dec == 'h':
                card,deck = hit(deck)
                p_hand.append(card)
                if hand_value(p_hand) > 21:
                    print(f'You lose.\nPlayer Hand: {p_hand}')
                    return
            
            elif p_dec == 's':
                p_turn = False
        
        while hand_value(p_hand)>hand_value(d_hand):
            if hand_value(d_hand) < 17:
                card, deck = hit(deck)
                d_hand.append(card)
            else:
                print(f'Congrats, you win!\n Player Hand: {p_hand}\nDealer Hand: {d_hand}')
                return
        
        if hand_value(d_hand) > 21:
            print(f'Congrats, you win!\n Player Hand: {p_hand}\nDealer Hand: {d_hand}')
            return
        elif hand_value(p_hand) < hand_value(d_hand):
            print(f'You lose.\n Player Hand: {p_hand}\nDealer Hand: {d_hand}')
            return
        
    