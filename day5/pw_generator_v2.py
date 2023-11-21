# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:43:35 2023

@author: jtazioli
Purpose: generate password using user input parameters
Inputs: # characters, # symbols, # numbers, 
Output: password
"""

#VERSION 2
#realized it would be so much better to concat lists of password feeders

import random as r



def password_generator():
    #get inputs
    #to do: QA for inputs
    num_char = int(input('How many characters is your password? '))
    
    num_symb = int(input('How many symbols do you want? '))
    
    num_numb = int(input('How many numbers do you want? '))
    
    num_alpha = num_char - (num_symb + num_numb)
    
    #references for possible password characters
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    symb_list = ['!','@','#','$','%','?']
    
    #holders for randomly selected  characters
    master_list = []
    
    #holder for password output
    output = ''
    
    #select characters to be used in password and store in holder lists
    for count in range(0,num_symb):
        master_list.append(symb_list[r.randint(0,len(symb_list)-1)])
    
    for count in range(0,num_numb):
        master_list.append(num_list[r.randint(0,len(num_list)-1)])
    
    for count in range(0,num_alpha):
        master_list.append(alpha_list[r.randint(0,len(alpha_list)-1)])
    
    print(master_list)
    
    for count in range(0,len(master_list)):
        dec1 = r.randint(0,len(master_list)-1)
        output += master_list.pop(dec1)
    
    return output