STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
from car_manager import CarManager

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.left(90)
        self.move_distance = MOVE_DISTANCE
        self.start_pos()

    def move_up(self):
        self.forward(self.move_distance)

    def start_pos(self):
        self.goto(STARTING_POSITION)


