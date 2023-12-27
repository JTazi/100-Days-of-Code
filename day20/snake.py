# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:22:57 2023

@author: jtazioli
"""
from turtle import Turtle

#x,y tuples with 3 part snake starting coordintes
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

        def __init__(self):
            #list to hold the snake segments as they're collected
            self.snake_parts = []
            self.create_snake()
            self.head = self.snake_parts[0]
            self.tail = self.snake_parts[-1]
            
        def create_snake(self):
            for position in STARTING_POSITIONS:
                self.add_segment(position)
                
        def add_segment(self,position):
            square = Turtle()
            square.shape('square')
            square.color('white')
            square.penup()
            square.setpos(x=position[0],y=position[1])
            self.snake_parts.append(square)
                
        def move(self):
            for x in range(len(self.snake_parts)-1,0,-1):
                new_pos = self.snake_parts[x-1].pos()
                self.snake_parts[x].setpos(x=new_pos[0],y=new_pos[1])
            self.snake_parts[0].forward(MOVE_DISTANCE)
            
        def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP)
        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)
        def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)
        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)
                
        def grow(self):
            tail_pos = self.tail.pos()
            self.add_segment(tail_pos)
            
        def game_over(self):
            for snake in self.snake_parts:
                snake.hideturtle()