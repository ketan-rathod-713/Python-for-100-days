#  How to create multiple turtles ? object states and instances !!

# Both are instances and can have different states attributes

#  Turtle race
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the rance ? Enter the color ?")

# center is 0 , 0 if height is 400 then -200 to 200
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
turtleDict = {}
for i in range(6):
    turtleDict[i] = Turtle(shape="turtle")
    turtleDict[i].penup()
    turtleDict[i].color(colors[i])
    j = i - 2.5
    turtleDict[i].goto(x=-220, y=50 * j)

if user_bet:
    is_race_on = True

while is_race_on:

    for i in turtleDict:
        if turtleDict[i].xcor() > 230:
            is_race_on = False
            winning_color = turtleDict[i].pencolor()
            # print(turtleDict[i].color())  , why it is giving two colors , one is pen color and other is fill color
            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} turtle is thw winner !")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        turtleDict[i].forward(random.randint(0, 20))

screen.exitonclick()

# Here i can also use list for storing turtles
