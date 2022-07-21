# Now in snake game , detect collision , create score board , detect collision with wall , detect collision with tail

# Inheritence
# class Fish(Animal):
# def __init__(self):
#     super().__init__()   Initialise everything that super class have
# Here fish is inheriting from animal


class Animal:
    def inhale(self):
        print("Inhale exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swimminhg")

    def inhale(self):
        super().inhale()
        print("just")  # To modify the inherited method


fish = Fish()
fish.swim()
fish.inhale()  # inherit method


# Previous snake continue..
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snack Game")

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.move()

    #distance method can be used if first segment and food are at distance 0 or less then certain amount 15
    if snake.head.distance(food) <= 15:
        snake.extend()
        food.refresh()
        scoreBoard.increase_score()

    # detect collision with wall
    # if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor < -280):
    #     game_is_on = False
    if(snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False
        scoreBoard.game_over()

    # detect tail collision
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            game_is_on = False
            scoreBoard.game_over()


screen.exitonclick()
