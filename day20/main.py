from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snack Game")

# There are some steps in making turtle game ==> make snack -> start moving it -> then add keyboard and collision
# with food ->start scoring

# tim = Turtle(shape="square")
# tim2 = Turtle(shape="square")
# tim3 = Turtle(shape="square")
#
# tim.color("white")
# tim2.color("white")
# tim3.color("white")
#
# tim2.goto(-20,0)
# tim3.goto(-40,0)


# Rather then we can use a tupple

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
# screen.tracer(0)
#
# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.penup()
#     new_segment.color("white")
#     new_segment.goto(position)
#     segments.append(new_segment)

# at first, it is showing weird behavior so we will use tracer here
# update the screen after all iteration , just like the gif works => composed of so many images
# first turn off the tracer and then when required do the stuff

# move 3rd block to the position of 2nd and 2nd block to the position of 1st and so on

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(.2)
#
#     for seg_no in range(len(segments)-1,0,-1):
#         new_x = segments[seg_no-1].xcor()
#         new_y = segments[seg_no-1].ycor()
#         segments[seg_no].goto(new_x,new_y)
#     segments[0].forward(20)
#     segments[0].left(90)
#

# Now move our data in oops form

snake = Snake()
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.3)

    snake.move()

screen.exitonclick()
