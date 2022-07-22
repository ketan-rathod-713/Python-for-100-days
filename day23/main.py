import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.move_up)

game_is_on = True
while game_is_on:
    time.sleep(.1) # item refreshed each .1 second
    screen.update()
    car_manager.move_cars()
    if time.time() - car_manager.prevTime > 2:
        car_manager.create_cars()

    # code for accident
    for car in car_manager.cars:
        if player.distance(car) < 10:
            # code for accident
            game_is_on = False

    # if car reached top most place then start from zero and increase speed
    if(player.ycor() > 200):
        player.start_pos()
        car_manager.increase_speed()
        scoreboard.increase_score()


turtle = Turtle()

screen.exitonclick()


# Break down the problem
# 1. move the cars randomly , then person turtle up and down