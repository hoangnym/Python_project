import turtle as t
import random

# timmy draws dashed line
# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colors = ["medium blue", "coral", "forest green",
          "brown", "red"]

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
    for _ in range(times):
        turtle.setheading(random.choice(angles))
        turtle.forward(30)
        turtle.speed("fastest")
        turtle.pensize(15)
        turtle.color(random.choice(colors))


# timmy = t.Turtle()
# timmy.shape("turtle")

# for shape_side in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)

tommy = t.Turtle()
random_walk(tommy, 500)


screen = t.Screen()
screen.exitonclick()