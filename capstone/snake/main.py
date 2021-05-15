# Import libraries
from turtle import Screen, Turtle
from snake import Snake
import time

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO: 1. Build snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# TODO: 2. Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for idx in range(len(segments) - 1, 0, -1):
        new_x = segments[idx - 1].xcor()
        new_y = segments[idx - 1].ycor()
        segments[idx].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


# TODO: 3. Create snake food

# TODO: 4. Detect collision with food

# TODO: 5. Create a scoreboard

# TODO: 6. Detect collision with wall

# TODO: 7. Detect collision with tail





screen.exitonclick()