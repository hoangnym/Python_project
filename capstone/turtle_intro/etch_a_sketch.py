import turtle as t

timmy = t.Turtle()

def forwards():
    timmy.forward(10)


def backwards():
    timmy.backward(10)


def counter_clockwise():
    timmy.right(10)
    timmy.forward(10)


def clockwise():
    timmy.left(10)
    timmy.forward(10)


def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = t.Screen()

screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.listen()

screen.exitonclick()