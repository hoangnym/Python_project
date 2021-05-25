import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
if __name__ == '__main__':
    window = tk.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=100)

    # Create and place tomato image
    canvas = tk.Canvas(width=200, height=224)
    tomato_img = tk.PhotoImage(file="tomato.png")
    canvas.create_image(103, 112, image=tomato_img)
    canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.pack()



    window.mainloop()