# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:53:04 2023

@author: jtazioli

Calculator:
    user inputs numbers and methods, program executes and returns final value
    calculations done iteratively, one at a time and user determines when it's complete
    

TO DO:
    - add qa/qc measures to ensure proper inputs
"""
def calculator():
    print('Caculator App:')
    
    cont_calc = True
    operation_lst = ['+','-','/','x']
    num = float(input('Starting Number:\n'))
    
    while cont_calc:
        operation = input(f'Operation: ({operation_lst})\n')
        second_num = float(input('Value: '))
        if operation == '+':
            num +=second_num
        elif operation == '-':
            num -+ second_num
        elif operation == '/':
            num = num / second_num
        elif operation == 'x':
            num = num * second_num
        cont = input("Are you done? (y/n) ")
        if cont == 'y':
            cont_calc = False
    
    return num


import operations as op

def calculator_v2():
    #create  function dictionary
    operation_dict = {'+':op.add,'-':op.subtract,'/':op.divide,'x':op.multiply}
    cont_calc = True
    num = float(input('Starting Number:\n'))
    
    while cont_calc:
        #use input to retreive function from dictionary
        operation = input(f'Operation: {list(operation_dict.keys())}\n')
        second_num = float(input('Value: '))
        #exectute function and store new value
        func = operation_dict[operation]
        num = func(num,second_num)
        #check user for end program
        cont = input("Are you done? (y/n) ")
        if cont == 'y':
            cont_calc = False
            
    return num

def calculator_v3():
    #add recursion so user can do new calculation without closing program
    #create  function dictionary
    operation_dict = {'+':op.add,'-':op.subtract,'/':op.divide,'x':op.multiply}
    cont_calc = True
    num = float(input('Starting Number:\n'))
    
    while cont_calc:
        #use input to retreive function from dictionary
        operation = input(f'Operation: {list(operation_dict.keys())}\n')
        second_num = float(input('Value: '))
        #exectute function and store new value
        func = operation_dict[operation]
        num = func(num,second_num)
        #check user for end program
        cont = input("Are you done? (y/n) or 'new' for new calculation. ")
        if cont == 'y':            
            cont_calc = False
            return num
        elif cont == 'new':
            cont_calc = False
            print(f'Output: {num}')
            print(f'Output: {calculator_v3()}')
            