import tkinter as tk

window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label",
                         font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"       # my_label.config(text="New Text")


# Button
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = tk.Entry(width=15)
input.pack()


window.mainloop()