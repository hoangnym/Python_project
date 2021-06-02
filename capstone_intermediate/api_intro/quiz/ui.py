import tkinter as tk


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.create_score_label()
        self.create_canvas()
        self.create_buttons()

        self.window.mainloop()


    def create_score_label(self):
        score_label = tk.Label(text=f"Score: {self.score}")
        score_label.grid(column=1, row=0)


    def create_canvas(self):
        canvas = tk.Canvas(width=250, height=300, highlightthickness=0)
        canvas.create_text(125, 150, font=("Arial", 20, "italic"))
        canvas.grid(column=0, row=1, columnspan=2)

    def create_buttons(self):
        # Red Button
        false_img = tk.PhotoImage(file="images/false.png")
        false_btn = tk.Button(image=false_img, highlightthickness=0)
        false_btn.grid(column=1, row=2)

        # Green Button
        true_img = tk.PhotoImage(file="images/true.png")
        true_btn = tk.Button(image=true_img, highlightthickness=0)
        true_btn.grid(column=0, row=2)