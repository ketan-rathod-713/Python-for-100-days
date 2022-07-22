from turtle import Turtle

FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.update_score()

    def update_score(self):
        self.reset()
        self.write(self.score, align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

