# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:31:26 2023

@author: jtazioli
"""

from turtle import Turtle, Screen
import random as r


def race_day():
    #init
    #clear previous turtles
    scr.resetscreen()
    #int counter for tracking turtle y coord
    counter = 1
    
    for t in t_lst:
        #raise pen
        t.penup()
        #make turtle turtle-shape
        t.shape('turtle')
        #establish size mode and imput width, height, outline
        t.resizemode('user')
        t.turtlesize(4,4,8)
        #select random color, (r,g,b)
        t.color((r.randint(0,255),r.randint(0,255),r.randint(0,255)))
        #move turtles to starting positions
        t.goto(init_x,(counter*spacing_y)+bot_y)
        counter += 1
    
    bet = scr.textinput(title="Make your bet!",prompt="Which turtle (1-6, bottom to top) will win?")
    #move
    race = True
    while race == True:
        #iterate through turtles and move forward random 1-40 pixels
        for t in t_lst:
            t.fd(r.randint(1,40))
            #check for turtle meeting winning conditions
            if t.xcor() > (win_w/2):
                race = False
                winner = t_lst.index(t)+1
            
    print(f"Turtle #{winner} wins! You bet on Turtle #{bet}.")
    scr.onkey(race_day,'space')    
    scr.listen()

#init turtle objects
t1,t2,t3,t4,t5,t6 = Turtle(),Turtle(),Turtle(),Turtle(),Turtle(),Turtle()
t_lst = [t1,t2,t3,t4,t5,t6]

#init screen object with title, color, and colormode
scr = Screen()
scr.title('Turtle Race')
scr.bgcolor('green')
scr.colormode(255)

#get window height and width could also use scr.setup to establish dimensions
win_w = scr.window_width()
win_h = scr.window_height()

init_x = (-(win_w/2)+20)
spacing_y = (win_h/7)
bot_y = -(win_h/2)

#race_day()
#every time I hit space the race_day function executes

scr.onkey(race_day,'space')    
scr.listen()

scr.mainloop()