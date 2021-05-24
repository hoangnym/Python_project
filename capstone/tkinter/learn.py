import tkinter as tk


def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


# Screen
window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)


# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button
new_button = tk.Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
input = tk.Entry(width=15)
input.grid(column=3, row=2)


window.mainloop()