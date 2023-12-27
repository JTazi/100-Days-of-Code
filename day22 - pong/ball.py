# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:45:39 2023

@author: jtazioli
"""
from turtle import Turtle

SPEED = 20

#create moving ball
class Pong_Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setpos(x=0,y=0)
        
    def northeast(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + SPEED
        new_y = current_y + SPEED
        self.goto(x=new_x,y=new_y)
        
    def northwest(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x - SPEED
        new_y = current_y + SPEED
        self.goto(x=new_x,y=new_y)
        
    def southeast(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + SPEED
        new_y = current_y - SPEED
        self.goto(x=new_x,y=new_y)
            
    def southwest(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x - SPEED
        new_y = current_y - SPEED
        self.goto(x=new_x,y=new_y)