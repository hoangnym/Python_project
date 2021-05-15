from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = -100

# Create new turtle instances
for idx in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[idx])
    turtle.penup()
    turtle.goto(x=-230, y=y_pos)
    y_pos += 40
    all_turtles.append(turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.x > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()