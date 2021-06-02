import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        # Score Label
        self.score_label = tk.Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Question
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=("Arial", 20, "italic"),
            text="Some Question Text",
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(
            image=true_img,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_btn.grid(column=1, row=2)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(
            image=false_img,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.update_score()
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        if is_right:
            self.score += 1

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        if is_right:
            self.score += 1

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

    def update_score(self):
        self.score_label["text"] = f"Score: {self.score}"


