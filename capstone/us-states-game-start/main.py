import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"]
print(states)


game_is_on = True
correct = 0

# while game_is_on:
answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What is another state's name?").capitalize()
print(answer_state)
if correct == 50:
    game_is_on = False


t.mainloop()