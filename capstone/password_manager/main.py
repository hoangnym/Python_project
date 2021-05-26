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
    canvas.grid(column=1, row=0)

    # Website row
    website_label = tk.Label(text="Website")
    website_label.grid(column=0, row=1)

    website_entry = tk.Entry(width=35)
    website_entry.grid(column=1, row=1, columnspan=2)

    # Email row
    email_label = tk.Label(text="Email/Username")
    email_label.grid(column=0, row=2)

    email_entry = tk.Entry(width=35)
    email_entry.grid(column=1, row=2, columnspan=2)






    window.mainloop()