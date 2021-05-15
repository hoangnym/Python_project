from turtle import Turtle


class Snake:

    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        segments = []
        for position in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)



