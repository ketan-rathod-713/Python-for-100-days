# today more on graphics
# see the turtle graphics documentation
# https://trinket.io/docs/colors
# https://docs.python.org/3/library/turtle.html
import random
import turtle
from turtle import Turtle, Screen
# from turtle import *
# Import everything , but avoid using it , if using one or two times then import whole module

# Aliasing module
# import turtle as t , so that next time we will write the short name

# installing module => internpreter => search and install setup
# or just write import followed by package name pycharm will automatically set up that

import heroes
print(heroes.gen())
# But sometimes if it is not bundled with python standard libray then manually install

timmy = Turtle()

timmy.shape("arrow")
# timmy.color("blue", "green")

# which color i can use search ==> tcl/Tk color / tkinter one of the ways to make GUI
# for _ in range(0,4):
#     timmy.forward(100)
#     timmy.right(90) # angle


# draw dashed line , in pen controll
t = Turtle()


# def dashedLine(total,space):
#     n = total
#     for i in range(n):
#         t.pendown()
#         t.forward(space)
#         t.penup()
#         t.forward(space)
#

# dashedLine(10,4)

# Now make square , then pentagon hexagon and so on
colors = ["red","blue","green"]
# make list long so that randomly assings color
# def makeShapes(sides):
#     angle = 360/sides
#     t.color(random.choice(colors))
#     for i in range(0,sides):
#         t.forward(100)
#         t.right(angle)
#     if sides<10:
#         makeShapes(sides+1)
#
# makeShapes(1)

# How to pick the random color
# Tuple is a data type in python  , (1,3,8) , it look a bit like list

my_tuple = (1,4,6)
print(my_tuple[0])
# why touple , you can't change the value of tupple , it is constant immutable
print(list(my_tuple)) # to create list from tuple

# color is defined by tuple bcz it is fixed
# Here we have to go in actual turtle module and change the color mode for that
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r, g, b)
    return randomColor

# Random walk , it is used in mathematics most of time , search path and so on see wikepedia


# directions = [90,180,270,360,-90,-180,-270,-360]
# t.speed(10)
# def randomWalk():
#     t.pensize(5)
#     t.color(random_color())
#     t.forward(20)
#     t.right(random.choice(directions))
#     randomWalk()

# randomWalk()


# Spirograph , draw a number of circles at a distance
# timmy.speed(20)
# def spirograph(gap):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(gap)
#     if not timmy.heading()==0:
#         spirograph(gap)
#
# spirograph(10)


#spot painting
# color gram package , exctract color from image
# get image in folder
# then figure out using it folder

import colorgram
colors = colorgram.extract('img.jpg', 30)
print(colors)

rgbColors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    current = (r, g, b)
    rgbColors.append(current)

print(rgbColors)

# 10 by 10 with radius 20 and space of 50

row = 10
column = 10
timmy.hideturtle()
def turnAround():
    timmy.backward(200)
    timmy.left(90)
    timmy.forward(20)
    timmy.right(90)

timmy.speed(20)
def drawHirstPaint(row,column):
    timmy.color(random.choice(rgbColors))
    if column==0:
        timmy.hideturtle()
        return
    if row==0:
        turnAround()
        drawHirstPaint(10,column-1)
    else:
        # timmy.pendown()
        timmy.dot(10)
        timmy.penup()
        timmy.forward(20)
        drawHirstPaint(row-1,column)


drawHirstPaint(row,column)

screen = Screen()
screen.exitonclick()
