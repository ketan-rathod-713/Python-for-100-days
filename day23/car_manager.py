import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

from turtle import Turtle


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.prevTime = time.time()

    def create_cars(self):
        self.prevTime = time.time()
        for i in range(0,random.randint(3,10)):
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(270+random.randint(0,100),random.randint(-200,200))
            car.setheading(180)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -200:
                self.cars.remove(car)
                car.reset()

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT







# How to think this code ?? I need to pass randomly cars from right to left
# first make random cars at right side then ask all of them to go forward