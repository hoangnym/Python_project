import pandas as pd
import tkinter as tk
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"



### <-------------------- UI SETUP ---------------------------> ###
if __name__ == '__main__':
    # Setup window
    window = tk.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    # Flashcard
    canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    front_card = tk.PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 268, image=front_card)
    canvas.grid(column=0, row=0, columnspan=2)

    # Red Button
    red_img = tk.PhotoImage(file="images/wrong.png")
    red_btn = tk.Button(image=red_img, highlightthickness=0)
    red_btn.grid(column=0, row=1)

    # Green Button
    green_img = tk.PhotoImage(file="images/right.png")












    window.mainloop()

