# PONG
# my idea

# One ball functionality ,two pullers, two obstacles, background and line

# 8 pieces
# create screen , create and move paddle , create another, create ball and move, detect collision and bounce, detect collision with paddle , detect when paddle misses , keep score
import time
from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)  # if it is there then we will need a while loop because we needed to update the screen manually each time
# Now make the paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # detect collision with paddle
    if ball.distance(r_paddle)< 50 and ball.xcor() > 335 or ball.distance(l_paddle)< 50 and ball.xcor() < -335 :
        ball.bounceX()

    #detect if the ball goes out of bounds at edge of the screen
    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
