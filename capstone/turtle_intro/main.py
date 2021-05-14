import turtle as t
import random

# timmy draws dashed line
# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colors = ["medium blue", "coral", "forest green",
#           "brown", "red"]


# Create random color RGB
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


# Draw different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    # Draw the figure
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


# Random walk
def random_walk(turtle, times):
    angles = [0, 90, 180, 270]
    turtle.pensize(15)
    turtle.speed("fastest")
    for _ in range(times):
        turtle.color(random_color())
        turtle.setheading(random.choice(angles))
        turtle.forward(30)


# timmy = t.Turtle()
# timmy.shape("turtle")

# for shape_side in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)

tommy = t.Turtle()
random_walk(tommy, 500)


screen = t.Screen()
screen.exitonclick()