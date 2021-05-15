# Import libraries
from turtle import Screen, Turtle

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

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
    for seg in segments:
        seg.forward(20)



# TODO: 3. Create snake food

# TODO: 4. Detect collision with food

# TODO: 5. Create a scoreboard

# TODO: 6. Detect collision with wall

# TODO: 7. Detect collision with tail





screen.exitonclick()