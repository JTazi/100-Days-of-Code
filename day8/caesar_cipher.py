# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:11:06 2023

@author: jtazioli

create a function called caesar cipher that shifts characters a given amount

inputs:
    decode/encode decision
    text message
    shift amount
outputs:
    shifted text
"""

alpha_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar_cipher(enc_dec, text, shift):
    output = ""
    #check if user inputs shift greater than the chars in the alphabet and reduce to actual net shift
    if shift >26:
        shift = shift % 26
        
    if enc_dec == 'encode':
        for char in text:
            #only shifting lower case letters, all else will be passed through
            if char in alpha_lst:
                new_ind = (shift + alpha_lst.index(char))
                if new_ind >25:
                    new_ind = new_ind-25
                    
                output += alpha_lst[new_ind]
            else:
                output += char
        return output
    
    elif enc_dec == 'decode':
        for char in text:
            #only shifting lower case letters, all else will be passed through
            if char in alpha_lst:
                new_ind = (alpha_lst.index(char) - shift)
                if new_ind < 0:
                    new_ind = new_ind + 25
                    
                output += alpha_lst[new_ind]
            else:
                output += char
        return output
    

def main():
    dec = input('Do you want to encode or decode your text? ("encode", "decode")\n').lower()
    text = input('What is your message?\n').lower()
    shift = int(input('What shift key do you want?\n'))
    
    output = caesar_cipher(dec,text,shift)
    
    print(f'Your message was: {text}\nYour message is now: {output}')