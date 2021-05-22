import turtle as t

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

t.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# t.onscreenclick(get_mouse_click_coor)

t.mainloop()