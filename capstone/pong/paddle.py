from turtle import Turtle

class Paddle:

    def __init__(self, x_pos, y_pos):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x_pos, y_pos)
        self.create_paddle()

    def create_paddle(self):
        self.paddle.pendown()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
