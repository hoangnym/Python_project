import tkinter as tk

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        # Score Label
        self.score_label = tk.Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Question
        self.canvas = tk.Canvas(width=250, height=300, bg="white")
        self.canvas.create_text(125, 150,
                           font=("Arial", 20, "italic"),
                           text="Some Question Text",
                           fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(column=1, row=2)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(column=0, row=2)

        self.window.mainloop()

