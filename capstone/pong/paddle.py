from turtle import Turtle, Screen

class Paddle:

    def __init__(self, x_pos, y_pos):
        self.paddle = Turtle()
        self.paddle.speed("fastest")
        self.paddle.penup()
        self.paddle.goto(x_pos, y_pos)
        self.paddle.color("white")
        self.create_paddle()

    def create_paddle(self):
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


