# import colorgram
#
#
# # Get color from image
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

rgb_colors = [(1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39), (216, 86, 63),
              (156, 6, 24), (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20),
              (175, 134, 162), (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85), (144, 227, 217),
              (121, 193, 147), (220, 177, 216), (100, 218, 229), (251, 198, 1), (116, 170, 192)]

# TODO: Paint a painting with 10 x 10 spots using Turtle
# Each point 20 in size and spaced apart by 50
t.colormode(255)


def starting_position(turtle):
    turtle.penup()
    turtle.goto(-200, -200)
    position = turtle.pos()
    return position


def draw_line_of_dots(turtle, num_dots, size_of_dot=50, gap=20):
    for _ in range(num_dots):
        # Create random color RGB
        turtle.pendown()
        turtle.dot(gap, random.choice(rgb_colors))
        turtle.penup()
        turtle.forward(size_of_dot)


def go_up_one_line(turtle, start, size_of_dot=50, gap=20):
    turtle.goto(start[0], start[1] + size_of_dot/2 + gap)
    position = turtle.pos()
    return position


# Initialize Turtle
painter = t.Turtle()
# Go to starting position
start = starting_position(painter)
grid_size = int(input("How large do you want the painting to be?: "))
# Draw line of dots
draw_line_of_dots(painter, grid_size)

for _ in range(grid_size):
    go_up_one_line(painter, start)
    draw_line_of_dots(painter, grid_size)

screen = t.Screen()
screen.exitonclick()

