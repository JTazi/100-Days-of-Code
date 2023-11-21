# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:16:55 2023

@author: jtazioli

#Silent Auction Program
add users and their bids until user dictates there are no more bids.
output the winner's name and bid.
clear console between entries.
"""
import os
import time

def silent_auction():
    auction = {}
    
    print('Welcome to the Silent Auction.')
    bid = input('Would you like to make a bid? (y / n)')

    while bid == 'y':
        name = input('Please enter your name:\n')
        bid_amount = int(input('Please enter your bid (rounded to whole dollar):\n'))
        
        auction[name] = bid_amount

        bid = input('Is there another bidder? (y / n)\n')
        os.system('cls')
        time.sleep(2)
    if len(auction) > 0:
        highest_bid = max(auction.values())
        winner = []
        for key in auction:
            if auction[key] == highest_bid:
                winner.append(key)
        
        if len(winner) == 1:
            print(f"The winner is: {winner[0]}\nHighest Bid: {highest_bid}")
        elif len(winner)>1:
            print(f"It's a draw! Highest bid is: {highest_bid}")
            print("The winners are:")
            for x in range(0,len(winner)):
                print(winner[x])
    else:
        print("No bidders for this item.")
        return
        

        
