# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:37:52 2023

@author: jtazioli
"""
#dependencies
from turtle import Screen
from overlay import Overlay
from playerpaddle import Player_Paddle
from ball import Pong_Ball
import time

#constants
P1_XCOORD = -540
P2_XCOORD = 540

#y coordinates
NORTH_BOUNDARY = 280
SOUTH_BOUNDARY = -280

#x coordinates
EAST_GOAL = 580
WEST_GOAL = -580

PADDLE_DISTANCE = 50

#main

#set up screen: x(-600,600), y(-300,300)
scr = Screen()
scr.setup(width = 1200,height = 600)
scr.bgcolor('black')
scr.title('Pong Game')
scr.tracer(n=0)

#establish UI
ui = Overlay()

#establish player paddles
paddle1 = Player_Paddle(P1_XCOORD)
paddle2 = Player_Paddle(P2_XCOORD)
scr.update()

#establish pong ball
ball = Pong_Ball()

#gameplay loop (listen for paddle moves and move ball)
scr.listen()
scr.onkey(paddle2.up,'Up')
scr.onkey(paddle2.down,'Down')
scr.onkey(paddle1.up,'w')
scr.onkey(paddle1.down,'s')

game_is_on = True
game_state = 0

#game_states:
    #0 - northeast
    #1 - southeast
    #2 - northwest
    #3 - southwest

while game_is_on:

    scr.update()
    time.sleep(0.1)
    
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    
#ALTERNATE METHOD:
#instead of using finite state machine logic I could have just recognized the pattern
#hitting the top wall inverses the change in y coordinates
#hitting the side paddles inverses the change in the x coordinates
#if ball_y >= NORTH_BOUNDARY:
#   y_modifier = y_modifier * (-1)    
    
    if game_state == 0:    
        #check for north boundary
        if ball_y >= NORTH_BOUNDARY:
            game_state = 1
        elif ball_x >= EAST_GOAL:
            #p1 scores point
            ui.score1 +=1
            ui.update_scoreboard()
            ui.draw_center_line()
            ball.home()
        elif ball.distance(paddle2) < PADDLE_DISTANCE:
            game_state = 2
            
        ball.northeast()
        
    elif game_state ==1:
        #check for south boundary
        if ball_y <= SOUTH_BOUNDARY:
            game_state = 0
        elif ball_x >= EAST_GOAL:
            #p1 scores point
            ui.score1 +=1
            ui.update_scoreboard()
            ui.draw_center_line()
            ball.home()
        elif ball.distance(paddle2) < PADDLE_DISTANCE:
            game_state = 3
            
        ball.southeast()
        
    elif game_state == 2:
        #check for north boundary
        if ball_y >= NORTH_BOUNDARY:
            game_state = 3
        elif ball_x <= WEST_GOAL:
            #p2 scores point
            ui.score2 +=1
            ui.update_scoreboard()
            ui.draw_center_line()
            ball.home()
        elif ball.distance(paddle1) < PADDLE_DISTANCE:
            game_state = 0

        ball.northwest()
        
    elif game_state == 3:
        #check for south boundary
        if ball_y <= SOUTH_BOUNDARY:
            game_state = 2
        elif ball_x <= WEST_GOAL:
            #p2 scores point
            ui.score2 +=1
            ui.update_scoreboard()
            ui.draw_center_line()
            ball.home()
        elif ball.distance(paddle1) < PADDLE_DISTANCE:
            game_state = 1
        
        ball.southwest()
        
    #game is played to 5, check scores and end game if necessary
    if ui.score1 == 5 or ui.score2 == 5:
        game_is_on = False
        ui.game_over()
        
    


scr.exitonclick()