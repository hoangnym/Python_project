import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

    # Detect when player has reached other side
    if turtle.finish():
        turtle.next_level()


screen.exitonclick()