import pandas as pd
import tkinter as tk
from tkinter import messagebox
import random

### <-------------------- Constants & data ---------------------------> ###
BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


### <-------------------- Generate new random word ---------------------------> ###
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_vocab, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_vocab, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


### <-------------------- UI SETUP ---------------------------> ###
if __name__ == '__main__':
    # Setup window
    window = tk.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    window.after(3000, func=flip_card)

    # Flashcard
    canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    front_card = tk.PhotoImage(file="images/card_front.png")
    back_card = tk.PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 268, image=front_card)
    card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
    card_vocab = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    # Red Button
    red_img = tk.PhotoImage(file="images/wrong.png")
    red_btn = tk.Button(image=red_img, highlightthickness=0, command=next_card)
    red_btn.grid(column=0, row=1)

    # Green Button
    green_img = tk.PhotoImage(file="images/right.png")
    green_btn = tk.Button(image=green_img, highlightthickness=0, command=next_card)
    green_btn.grid(column=1, row=1)

    next_card()

    window.mainloop()

