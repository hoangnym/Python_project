import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
colors = ["medium blue", "coral", "forest green"]

# timmy draws dashed line
# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# Let timmy draw triangle up to decagon
def draw_shape(num_sides):
    angle = 360 / num_sides
    # Draw the figure
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side)

screen = t.Screen()
screen.exitonclick()