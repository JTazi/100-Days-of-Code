# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 08:01:16 2023

@author: jtazioli
"""

from turtle import Turtle, Screen
import random
import colorgram


def get_colors():
    color_lst = []
    # Extract 6 colors from an image.
    colors = colorgram.extract('resources/starry-night.jpg', 6)

    # colorgram.extract returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color.
    for color in colors:
        rgb = color.rgb # e.g. (255, 151, 210)
        color_lst.append(rgb)
    
    return  color_lst

def draw_shape(sides,turtle):
    angle = 360 / sides
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    turtle.pencolor(r,g,b)
    
    for x in range(sides):
        t.forward(100)
        t.right(angle)

def walk(turtle):
    direction = random.randint(0,2)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    turtle.pencolor(r,g,b)
    
    if direction == 0:
        turtle.left(90)
        turtle.forward(25)
    elif direction == 1:
        turtle.forward(25)
    elif direction == 2:
        turtle.right(90)
        turtle.forward(25)

def draw_row():
    counter = 0
    while counter < dpr:
        t.forward(w/(dpr+1))
        dot_color = color_list[random.randint(0,5)]
        t.dot(ds,dot_color)
        counter +=1

#canvas height and width
w = 200
h = 200

#num of dots per row and num of rows
dpr = 10
dpc = 10

#dot size
ds = 20

#counter for columns
row_counter = 1

#get img colors
color_list = get_colors()

t = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(w,h)
screen.setworldcoordinates(0,0,w,h)

t.pensize(7)
t.penup()
t.shape('turtle')
#t.turtlesize()
t.st()
t.setpos(0,(row_counter * (h/(dpc+1))))

while row_counter <=  dpc+1:
    draw_row()
    t_y = (row_counter * (h/(dpc+1)))
    t.goto(0,t_y)
    row_counter +=1
        
screen.exitonclick()

