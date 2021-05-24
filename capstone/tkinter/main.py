# Create a mile to km converter using tkinter and gui
import tkinter as tk


# Set up window
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


# Use grid system to place modules
# input module for user (miles)
user_input = tk.Entry()
user_input.grid(column=1, row=0)


# miles label
miles_label = tk.Label()
miles_label["text"] = "miles"
miles_label.grid(column=2, row=0)


# equal label
equal_label = tk.Label()
equal_label["text"] = "is equal to"
equal_label.grid(column=0, row=1)


# output label
output_label = tk.Label()
output_label["text"] = 0
output_label.grid(column=1, row=1)


# km label


window.mainloop()