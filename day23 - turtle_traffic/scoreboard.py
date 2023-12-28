from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_X = -150
SCORE_Y = 250

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.hideturtle()
        self.color("black")
        
        #initialize score
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.speed('fastest')
        
        self.goto(x=SCORE_X,y=SCORE_Y)
        self.write(str(self.score),align='center',font=FONT)
        
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("Game Over",align = 'center', font=FONT)
