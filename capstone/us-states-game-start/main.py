import turtle as t
import pandas as pd

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
        if (answer_state in states) and (answer_state not in correct_answers):
            correct_answers.add(answer_state)
    print(correct_answers, len(correct_answers))

screen.exitonclick()

# t.mainloop()