# Using screen events
# listen method to listen to the events

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def counter_clockwise():
    tim.left(20)


def clockwise():
    tim.right(20)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def draw_circle():
    for i in range(0,9):
        move_forwards()
        counter_clockwise()


def color_red():
    tim.color("red")


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="h", fun=draw_circle)
screen.onkey(key="r",fun=color_red)



screen.exitonclick()  # put it at last for code to work why ??







# Passing function to another function

def add(n1,n2):
    return n1+n2


def sub(n1,n2):
    return n1-n2

# Similarly other functions like multiply and all
def calculator(n1,n2,func):
    return func(n1,n2)


print(calculator(2,3,add))
print(calculator(2,3,sub))

# Higher order function
# Function that is working with the other functions like calculator here

