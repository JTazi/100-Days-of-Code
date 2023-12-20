# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:04:48 2023

@author: jtazioli
"""

from turtle import Turtle, Screen

t = Turtle()
scr = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.forward(-10)
    
def turn_left():
    t.left(5)
    
def turn_right():
    t.right(5)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

scr.listen()
scr.onkey(fun=move_forward,key="w")
scr.onkey(fun=move_backward,key="s")
scr.onkey(fun=turn_left,key="a")
scr.onkey(fun=turn_right,key="d")
scr.onkey(fun=clear,key="c")

scr.exitonclick()

