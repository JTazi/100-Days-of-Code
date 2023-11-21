# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:40:53 2023

@author: jtazioli
"""
import resources as r


dec1_inputs = ['left','right']
dec2_inputs = ['left','right','straight']

def input_check(str_in,str_des):
    if str_in in str_des:
        return True
    else:
        return False



def word_game():
    print(r.zoo)
    print(r.gate)
    
    dec1=str(input('Welcome to the Zoo! You enter the front gate. Do you go "Left" or "Right"?')).lower()
    
    while input_check(dec1,dec1_inputs)==False:
        dec1=str(input('Try again, do you go "Left" or "Right"?')).lower()
    
    if dec1 == 'left':
        print('You go left, run into a herd of elephants and are forced to flee from the park.')
        print(r.elephants)
        return
        
        
    elif dec1 == 'right':
        dec2 = input('You follow the path to the right and are presented with an intersection. You can go "Straight", "Left", or "Right"')
        while input_check(dec2,dec2_inputs) == False:
            dec2 = str(input('You follow the path to the right and are presented with an intersection. You can go "Straight", "Left", or "Right"')).lower()
        if dec2 == 'straight':
            print('You go straight, fall into a hole and are trapped forever.')
            return
        elif dec2 == 'left':
            print('You go left, run into an ankylosaurus and are forced to flee from the park.')
            print(r.ankyl)
            return
        elif dec2 == 'right':
            print('You found the llamas, you WIN!!!')
            print(r.llamas)
            return
    
    































