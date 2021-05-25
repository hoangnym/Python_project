import tkinter as tk
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.025
LONG_BREAK_MIN = 0.05
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM -------------------------------
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
if __name__ == '__main__':
    window = tk.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=100, bg=YELLOW)

    # Create title
    title = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "normal"))
    title.grid(column=1, row=0)

    # Create and place tomato image
    canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = tk.PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    # create start button
    start_btn = tk.Button(text="Start", command=start_timer)
    start_btn.grid(column=0, row=2)

    # create reset button
    reset_btn = tk.Button(text="Reset", command=reset_timer)
    reset_btn.grid(column=2, row=2)

    # check mark
    tick_mark = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "normal"))
    tick_mark.grid(column=1, row=3)


    window.mainloop()