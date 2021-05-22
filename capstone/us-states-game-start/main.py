import turtle as t

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What is another state's name?")
print(answer_state)


t.mainloop()