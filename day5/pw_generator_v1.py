# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:25:25 2023

@author: jtazioli

Purpose: generate password using user input parameters
Inputs: # characters, # symbols, # numbers, 
Output: password
"""
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
    
    #holders for randomly selected password characters
    output_symb = []
    output_alpha = []
    output_num = []
    
    master_list = [output_symb,output_alpha,output_num]
    
    #holder for password output
    output = ''
    
    #select characters to be used in password and store in holder lists
    for count in range(0,num_symb):
        output_symb.append(symb_list[r.randint(0,len(symb_list)-1)])
    
    for count in range(0,num_numb):
        output_num.append(num_list[r.randint(0,len(num_list)-1)])
    
    for count in range(0,num_alpha):
        output_alpha.append(alpha_list[r.randint(0,len(alpha_list)-1)])
        
    #print(f'Symbols: {output_symb}\nNumbers: {output_num}\nAlpha: {output_alpha}')    
    
    #iterate number of times based on password length
    #detect once all required characters have been used
    for count in range(0,num_char):
        if output_symb !=[] and output_alpha != [] and output_num != []:
            dec1 = r.randint(0,2)
            dec2 = r.randint(0,len(master_list[dec1])-1)
            output += master_list[dec1].pop(dec2)
        
        else:
            counter = 0
            for lst in master_list:
                if lst == []:
                    del master_list[counter]
                counter +=1
            
            if len(master_list) == 2:
                
                if master_list[0] != [] and master_list[1] != []:
                    dec1 = r.randint(0,1)
                    dec2 = r.randint(0,len(master_list[dec1])-1)
                    output += master_list[dec1].pop(dec2)
            else:
                for char in master_list[0]:
                    output+=char
                return output
                