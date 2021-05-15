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
snake = Snake(3)

# TODO: 2. Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move(5)


# TODO: 3. Create snake food

# TODO: 4. Detect collision with food

# TODO: 5. Create a scoreboard

# TODO: 6. Detect collision with wall

# TODO: 7. Detect collision with tail





screen.exitonclick()