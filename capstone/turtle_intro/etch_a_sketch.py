import turtle as t


def forwards(turtle):
    turtle.forward(10)


def backwards(turtle):
    turtle.backward(10)


def counter_clockwise(turtle):
    turtle.seth(to_angle=5)
    turtle.forward(10)


def clockwise(turtle):
    turtle.seth(to_angle=355)
    turtle.forward(10)


def clear_drawing(turtle):
    turtle.clearsreen()


timmy = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()