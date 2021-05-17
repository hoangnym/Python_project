from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# TODO: 1) Create the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()
# TODO: 2) Create and move a paddle
paddle_right = Paddle((350, 0))
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

# TODO: 3) Create another paddle
paddle_left = Paddle((-350, 0))
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

# TODO: 4) Create the ball and make it move
ball = Ball()

# TODO: 8) Keep score
score = Scoreboard()


game_is_on = True
sleep_time = 0.05

while game_is_on:
    time.sleep(max(0.001, sleep_time))
    screen.update()
    ball.move()

    # TODO: 5) Detect collision with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_of_wall()

    # TODO: 6) Detect collision with paddles
    if (ball.xcor() >= 330 and ball.distance(paddle_right) < 50) or (ball.xcor() <= -330 and ball.distance(paddle_left) < 50):
        ball.bounce_of_paddle()
        sleep_time -= 0.005

    # TODO: 7) Detect ball out of bounds
    if ball.xcor() > 400:
        ball.reset()
        score.point_left()
        sleep_time = 0.05

    if ball.xcor() < -400:
        ball.reset()
        score.point_right()
        sleep_time = 0.05


screen.exitonclick()