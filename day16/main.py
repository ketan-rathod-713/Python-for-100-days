
# Object oriented programming

# As the complexity increases , procedural programming becomes inefficient so we divide our code into objects
# Like that of car , different types of properties and several modules to work on

# We can split our code between two teams by dividing the sub modules like let one team focus on this object and other on other

# We can reuse our code

# if you are one person who do waiter and chef work and all but it is for small restorant but for bigger one we need to higher
# the peope who are good at their work

# What waiter has and what waiter does do , attributes and it's methods

# method is function of object
# Blueprint is class and it's instances are objects

# already implemented module
# import turtle
#
# timmy = turtle.Turtle()

from turtle import Turtle,Screen

timmy = Turtle() # This is good way of writting but may be first one is also good
timmy.shape("turtle") # Now it will show actual turtle rather then arrow
timmy.color("red")

timmy.forward(100)
timmy.circle(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick() # Now our code only exit when we click on the screen

# https://docs.python.org/3/library/turtle.html
