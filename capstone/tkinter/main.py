import tkinter as tk

window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label",
                         font=("Arial", 24, "bold"))
my_label.pack(side="left")
my_label["text"] = "New Text"       # my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()