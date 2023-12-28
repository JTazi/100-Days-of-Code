import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#constants
SPAWN_FREQUENCY = 10

#initialize turtle screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

#initialize score
sb = Scoreboard()

#initialize player
player = Player()

#initialize cars
cm = CarManager()

#gameplay loop (listen for paddle moves and move ball)
screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
spawn_counter = 10

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cm.move_car()
    
    #check for making it to the top
    if player.win():
        #move player back to start
        player.reset()
        #clear the cars
        cm.reset()
        #update score
        sb.score+=1
        sb.update_scoreboard()
    
    #check for car collision
    if cm.check_collision(player.position()):
        game_is_on = False
    
    #check for if it's time to spawn car
    if spawn_counter == SPAWN_FREQUENCY:
        cm.create_car()
        spawn_counter = 0
    
    spawn_counter +=1

#game is over
sb.game_over()

screen.exitonclick()