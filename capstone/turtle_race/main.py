from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = -100

for idx in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[idx])
    turtle.penup()
    turtle.goto(x=-230, y=y_pos)
    y_pos += 40


screen.exitonclick()