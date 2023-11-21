# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:04:38 2023

@author: jtazioli

#Band Name Generator
Receive user input for pet name and city of origin then output the combination
"""

#get user city of origin
city = input('What city were you born?\n')

#get user first pet name
pet_name = input('What was the name of your first pet?\n')

#output combo
band_name = (city.lower() + " " + pet_name.lower()).title()
print(f'Your band name is: {band_name}')