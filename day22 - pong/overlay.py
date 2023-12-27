# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:52:58 2023

@author: jtazioli
"""

#pong overlay
from turtle import Turtle

P1_SCORE_X = -50 
P1_SCORE_Y = 260
P2_SCORE_X = 50
P2_SCORE_Y = 260
SCORE_FONT = ('Arial',20,'normal')
END_FONT = ('Arial',30,'normal')

class Overlay(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        
        self.hideturtle()
        self.color('white')
        
        #draw center line
        self.draw_center_line()
        
        #initialize scoreboard
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.speed('fastest')
        
        self.goto(x=P1_SCORE_X,y=P1_SCORE_Y)
        self.write(str(self.score1),align='center',font=SCORE_FONT)
        
        self.goto(x=P2_SCORE_X,y=P2_SCORE_Y)
        self.write(str(self.score2),align='center',font=SCORE_FONT)

    def draw_center_line(self):
        #starting at (0,-300), every 20 pixels, draw a 10 pixel line
        self.penup()
        self.goto(x=0,y=-300)
        self.setheading(90)
        for y_val in range(-280,300,20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.goto(x=0,y=y_val)
            
    def game_over(self):
        self.goto(x=0,y=50)
        if self.score1 == 5:    
            self.write("Player 1 Wins!",align = 'center', font=END_FONT)
        else:
            self.write("Player 2 Wins!", align = 'center',font=END_FONT)
            