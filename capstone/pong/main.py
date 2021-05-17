from turtle import Turtle, Screen
from paddle import Paddle


# TODO: 1) Create the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# TODO: 2) Create and move a paddle
paddle_right = Paddle(350, 0)
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

# TODO: 3) Create another paddle
paddle_right = Paddle(-350, 0)
screen.onkey(paddle_right.go_up, "w")
screen.onkey(paddle_right.go_down, "s")

# TODO: 4) Create the ball and make it move

# TODO: 5) Detect collision with wall and bounce

# TODO: 6) Detect collision with paddle

# TODO: 7) Detect collision with paddle

# TODO: 8) Keep score


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()