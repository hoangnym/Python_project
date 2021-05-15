from turtle import Turtle


class Snake:

    def __init__(self, num_segs=3):
        self.num_segs = num_segs
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_positions = []
        x_pos = 0
        y_pos = 0
        for i in range(self.num_segs):
            starting_positions.append((x_pos, y_pos))
            x_pos -= 20
        for position in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self, move_dist):
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        self.head.seth(90)

    def down(self):
        self.head.seth(270)

    def left(self):
        self.head.seth(180)

    def right(self):
        self.head.seth(0)



