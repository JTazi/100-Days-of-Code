import turtle
import pandas as pd

IMAGE = 'blank_states_img.gif'
FONT = ("Courier", 10, "normal")

df = pd.read_csv('50_states.csv')

#only needed once to get x,y grids
states = df.state.tolist()

game_on = True
guessed = []
num_right = 0
# x = []
# y = []

# def get_click_loc(x,y):
#     x.append(x)
#     y.append(y)


class Answer_Bot(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        
    def add_label(self,x,y,state):
        self.speed('fastest')
        self.goto(x,y)
        self.write(state,align='center',font=FONT)

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)
ab = Answer_Bot()

while game_on:
    #the game, ask user for input and populate map if it's a new guess
    answer_state = screen.textinput(f"{num_right}/50 - Guess State:","Name a state:")
    
    if answer_state not in guessed and answer_state in states:
        x = df[df.state == answer_state]['x'].iloc[0]
        y = df[df.state == answer_state]['y'].iloc[0]
        ab.add_label(x,y,answer_state)
        guessed.append(answer_state)
        num_right += 1
        
    elif answer_state in guessed:
        answer_state = screen.textinput(f"{num_right}/50 - Guess State:","Already Guessed that, guess again:")
        
    elif answer_state == 'done':
        game_on = False
        df_tolearn = df[~df.state.isin(guessed)]
        df_tolearn.to_csv('states_to_study.csv')
        
    
    
    #go through and click states in alphabetical order to get x,y grids for labels
    #store in lists and then save to .csv
    # turtle.onscreenclick(get_click_loc)
    # turtle.mainloop()
screen.exitonclick()