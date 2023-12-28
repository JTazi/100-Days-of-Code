from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.showturtle()
        self.shape('turtle')
        self.color('green')
        self.resizemode('user')
        self.turtlesize(2,2,1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
    
    def reset(self):
        self.goto(STARTING_POSITION)
