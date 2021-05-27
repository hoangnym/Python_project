import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# TODO: Generate a password with certain rules


# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO: Take User inputs and when "add" clicked saved to text file: (data.txt) => website | email | pw
# clear screen after saving to screen (delete() method)
def save():
    with open("data.txt", mode="a") as pw_file:
        url = website_entry.get()
        email = email_entry.get()
        pw = password_entry.get()
        pw_file.write(f"{url} | {email} | {pw} \n")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


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
    website_label = tk.Label(text="Website:")
    website_label.grid(column=0, row=1)

    website_entry = tk.Entry(width=35)
    website_entry.grid(column=1, row=1, columnspan=2)
    website_entry.focus()

    # Email row
    email_label = tk.Label(text="Email/Username:")
    email_label.grid(column=0, row=2)

    email_entry = tk.Entry(width=35)
    email_entry.grid(column=1, row=2, columnspan=2)
    email_entry.insert(0, "hoang.1994@ymail.com")

    # Password row
    password_label = tk.Label(text="Password:")
    password_label.grid(column=0, row=3)

    password_entry = tk.Entry(width=21)
    password_entry.grid(column=1, row=3)

    generate_btn = tk.Button(text="Generate Password")
    generate_btn.grid(column=2, row=3)

    # Add to file
    add_btn = tk.Button(text="Add", width=36, command=save)
    add_btn.grid(column=1, row=4, columnspan=2)

    window.mainloop()