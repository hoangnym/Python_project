import turtle as t
import pandas as pd
from map import Map

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

df = pd.read_csv("50_states.csv")
states = set(df["state"])
correct_answers = set()

game_is_on = True
while game_is_on:
    score = len(correct_answers)
    if score == 50:
        game_is_on = False
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What is another state's name?").title()
        if answer_state == "Exit":
            # states_to_learn.csv
            states_to_learn = list(states - correct_answers)
            learn_df = pd.DataFrame(states_to_learn)
            learn_df.to_csv("states_to_learn.csv")
            break
        if (answer_state in states) and (answer_state not in correct_answers):
            correct_answers.add(answer_state)
            x_cor = int(df[df['state'] == answer_state].x)
            y_cor = int(df[df['state'] == answer_state].y)
            Map(answer_state, x_cor, y_cor)

screen.exitonclick()

# t.mainloop()