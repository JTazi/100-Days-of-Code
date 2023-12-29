# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:28:59 2023

@author: tazma
"""

#constants
NAMES_FILE = './input/names.txt'

def make_invitations():
    with open(NAMES_FILE,mode = 'r') as file:
        names_list = file.read().split('\n')
    
    for name in names_list:
        with open(f'./output/invite_{name}.txt', mode='w') as file:
            data = f'Dear {name},\nYou are invited to my party.\nSincerely,\nJT'
            file.write(data)