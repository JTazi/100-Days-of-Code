# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:49:57 2023

@author: jtazioli

Improvements:
    1. qa on user inputs
    2. off/report able to be queried at any input
    3. stop asking for change inputs once enough money is input
"""
#constants
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}



#functions
def report(res, money):
    print(f"Water: {res['water']}\nMilk: {res['milk']}\nCoffee: {res['coffee']}\nMoney: ${money}")
    
def check_res(drink, res):
    #check resource costs  for drink against available resources
    #return true if sufficient available resources
    res_dict = MENU[drink]['ingredients']
    for ingredient in res_dict:
        if res[ingredient] < res_dict[ingredient]:
            return False
    return True

def make_coffee(res,drink):
    for item in MENU[drink]['ingredients']:
        res[item] -= MENU[drink]['ingredients'][item]
    return res
    
    
def get_payment():
    q = int(input("How many quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickels?"))
    p = int(input("How many pennies?"))
    
    total = round((.25*q)+(.10*d)+(.05*n)+(.01*p),2)
    return total

def main():
    #variables
    state = 'init'
    money = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    running = True
    
    while running == True:
        if state == 'init':
            print("Coffee Machine:")
            order = input('What would you like? (espresso/latte/cappuccino)')
            drink_answers = ['espresso','latte','cappuccino']
            if order in drink_answers:
                state = 'drink'
            elif order == 'off':
                running = False
            elif order == 'report':
                report(resources,money)
            
        elif state == 'drink':
            #if customer orders drink:
                #1. check if resources available
                #2. prompt user for coins
                #3. check if money sufficient
                #4. dispense drink
            if check_res(order, resources):
                #resources available, prompt for payment
                payment = get_payment()
                if payment < MENU[order]['cost']:
                    print(f"You inserted ${payment}, the drink is ${MENU[order]['cost']}. Money refunded.")
                    state = 'init'
                else:
                    change = round(payment-MENU[order]['cost'],2)
                    if change != 0:
                        print(f'You inserted ${payment}, your change is ${change}.')
                    money+=MENU[order]['cost']
                    resources = make_coffee(resources,order)
                    print(f"Here's your {order}.")
                    state = "init"
            else:
                print("Not enough resources.Please notify staff.")
                state = 'init'
                
                