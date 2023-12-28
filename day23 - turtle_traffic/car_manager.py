from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_X = 290
LANES = range(-260,260,20)

class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()
        
    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape('square')
        car.setheading(180)
        car.color(COLORS[r.randint(0,5)])
        car.resizemode('user')
        car.shapesize(1,3,1)
        car.setposition(x = SPAWN_X, y = LANES[r.randint(0,len(LANES)-1)])
        
        self.car_list.append(car)
        
    def move_car(self):
        for car in self.car_list:
            car.forward(self.move_distance)
            
    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT
        
    def check_collision(self,player_position):
        #player position is (x,y) tuple
        for car in self.car_list:
            if car.distance(player_position) < 20:
                return True
            else:
                pass
    
    def reset(self):
        for car in self.car_list:
            car.reset()
            car.hideturtle()
        self.car_list = []
        self.increase_move_distance()