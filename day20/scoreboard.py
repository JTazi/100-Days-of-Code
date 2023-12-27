# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:24:32 2023

@author: jtazioli
"""
from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'
FONT_SIZE = 16
FONT_TYPE = 'normal'

GAME_OVER_FONT_SIZE = 24

class Score_Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0,y=275)
        self.speed('fastest')
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f'Score: {self.score}',align='center',font=(FONT,FONT_SIZE,FONT_TYPE))
    
    def plus_one(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.home()
        self.write("Game Over.",align = 'center',font=(FONT,GAME_OVER_FONT_SIZE,FONT_TYPE))
        