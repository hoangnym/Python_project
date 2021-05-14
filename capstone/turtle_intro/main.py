from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

# timmy draws dashed line
# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Let timmy draw triangle up to decagon
for i in range(3, 11):
    angle = 360 / i
    # Draw the figure
    for _ in range(i):
        timmy.forward(100)
        timmy.right(angle)


screen = Screen()
screen.exitonclick()