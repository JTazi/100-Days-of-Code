# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:30:40 2023

@author: jtazioli
"""
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score_Board

FOOD_COLLISION_DISTANCE = 15

scr = Screen()
scr.setup(width = 600,height = 600)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(n=0)

snake = Snake()
food = Food()

scr.listen()
scr.onkey(snake.up,'Up')
scr.onkey(snake.down,'Down')
scr.onkey(snake.left,'Left')
scr.onkey(snake.right,'Right')

game_is_on = True
sb = Score_Board()

while game_is_on:

    scr.update()
    time.sleep(0.2)
    snake.move()
    
    #detect collision with food with turtle.distance
    if snake.head.distance(food) < FOOD_COLLISION_DISTANCE:
        food.refresh()
        snake.grow()
        sb.plus_one()
    
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        
        #change so that game resets instead of ends
        #game_is_on = False
        #snake.game_over()
        #sb.game_over()
        snake.reset()
        sb.reset()

        
    #detect collision with self
    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 10:
            #change so that game resets instead of ends
            #game_is_on = False
            #snake.game_over()
            #sb.game_over()
            snake.reset()
            sb.reset()




scr.exitonclick()