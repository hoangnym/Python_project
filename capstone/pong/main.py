from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
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


game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # TODO: 5) Detect collision with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_of_wall()

    # TODO: 6) Detect collision with paddles
    if (ball.xcor() >= 340 and ball.distance(paddle_right) < 50) or (ball.xcor() <= -340 and ball.distance(paddle_left) < 50):
        ball.bounce_of_paddle()


screen.exitonclick()