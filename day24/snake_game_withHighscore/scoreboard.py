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

PLAYER_SCORE_COORD = (-75, 275)
HIGH_SCORE_COORD = (75, 275)

HIGH_SCORE_FILENAME = 'SNAKE_HIGH_SCORE.txt'

class Score_Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open(HIGH_SCORE_FILENAME, mode = 'r') as file:
            self.high_score = int(file.read())
        
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(PLAYER_SCORE_COORD)
        self.write(f'Score: {self.score}',align='center',font=(FONT,FONT_SIZE,FONT_TYPE))
        self.goto(HIGH_SCORE_COORD)
        self.write(f'High Score: {self.high_score}',align='center',font=(FONT,FONT_SIZE,FONT_TYPE))
    
    def plus_one(self):
        self.score += 1
        self.update_scoreboard()
        
    #instead of game over, reset and update high_score
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_FILENAME, mode = 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.home()
    #     self.write("Game Over.",align = 'center',font=(FONT,GAME_OVER_FONT_SIZE,FONT_TYPE))
        