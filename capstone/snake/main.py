# Import libraries
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO: 1. Build snake body
snake = Snake(3)

# TODO: 3. Create snake food
food = Food()

# TODO: 5. Create a scoreboard
scoreboard = Scoreboard()

# TODO: 2. Move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075)
    snake.move(20)

    # TODO: 4. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()


# TODO: 6. Detect collision with wall

# TODO: 7. Detect collision with tail





screen.exitonclick()