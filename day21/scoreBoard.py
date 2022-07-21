

# It will also inherite the turtle class as we can display something on scrren using write method of turtle

# Now the font size is 15
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-20, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", font=("Verdana", 15, "normal"))

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=("Verdana", 15, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=("Verdana", 15, "normal"))
