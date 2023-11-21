# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 08:08:07 2023

@author: jtazioli

TIP CALCULATOR:
    input cost of total bill
    input percentage of tip
    output cost per person
"""

tot_cost = float(input("What is the cost of the bill?\n"))
tip_percent = float(input("What percent do you want to  leave as tip? (ex. 10, 15, 20)\n"))
num_people = int(input("How many people are splitting the bill?\n"))

tip = round(tot_cost * (tip_percent/100),2)
tip_per_person = round(tip / num_people,2)

print(f"Each person pays: ${tip_per_person} for a {tip_percent}% tip.")