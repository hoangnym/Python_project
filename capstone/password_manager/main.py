import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# TODO: Generate a password with certain rules
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    pw_symbols = [random.choice(symbols) for letter in range(random.randint(2, 4))]
    pw_numbers = [random.choice(numbers) for letter in range(random.randint(2, 4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO: Take User inputs and when "add" clicked saved to text file: (data.txt) => website | email | pw
# clear screen after saving to screen (delete() method)
def save():
    url = website_entry.get()
    email = email_entry.get()
    pw = password_entry.get()
    
    if len(url) == 0 or len(pw) == 0:
        empty = messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=url, message=f"These are your details entered: \nEmail: {email} "
                                              f"\nPassword: {pw} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as pw_file:
                pw_file.write(f"{url} | {email} | {pw}\n")
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

    generate_btn = tk.Button(text="Generate Password", command=password_generator)
    generate_btn.grid(column=2, row=3)

    # Add to file
    add_btn = tk.Button(text="Add", width=36, command=save)
    add_btn.grid(column=1, row=4, columnspan=2)

    window.mainloop()