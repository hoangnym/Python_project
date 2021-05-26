import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
if __name__ == '__main__':
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    # Create a password image on screen
    canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
    lock_img = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=lock_img)
    canvas.pack()






    window.mainloop()