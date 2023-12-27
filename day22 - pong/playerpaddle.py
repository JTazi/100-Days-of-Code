# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:14:16 2023

@author: jtazioli
"""
from  turtle import Turtle
#player paddle objects using Turtle()




#stretch perpendicular to orientation, oriented east by default
STRETCH_WIDTH = 4

class Player_Paddle(Turtle):
    
    def __init__(self,x_coord):
        super().__init__()
        self.showturtle()
        self.shape('square')
        self.resizemode('user')
        self.shapesize(stretch_wid = STRETCH_WIDTH,stretch_len = 1.2,outline = 1)
        self.color('white')
        self.penup()
        self.setpos(x=x_coord,y=0)
        
        
    def up(self):
        current_y = self.ycor()
        current_x = self.xcor()
        new_y = current_y + 40
        
        #keep player from moving paddle off top screen
        if current_y < 560:
            self.goto(current_x,new_y)

        
    def down(self):
        current_y = self.ycor()
        current_x = self.xcor()
        new_y = current_y - 40

        #keep player from moving paddle off bottom screen        
        if current_y > -560:
            self.goto(current_x,new_y)

        
