# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:13:23 2023

@author: jtazioli
"""
from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.goto(x=r.randint(-280,280),y=r.randint(-280,280))
        
    def refresh(self):
        random_x = r.randint(-280,280)
        random_y = r.randint(-280,280)
        self.goto(random_x,random_y)