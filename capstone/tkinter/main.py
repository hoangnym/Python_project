# Create a mile to km converter using tkinter and gui
import tkinter as tk

def miles_to_km():
    miles = float(user_input.get())
    km = 1.60934 * miles
    output_label["text"] = km
    return miles, km


if __name__ == '__main__':
    # Set up window
    window = tk.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=10, pady=10)

    # Use grid system to place modules
    # input module for user (miles)
    user_input = tk.Entry()
    user_input.config(width=9)
    user_input.grid(column=1, row=0)

    # miles label
    miles_label = tk.Label(text="miles")
    miles_label.grid(column=2, row=0)

    # equal label
    equal_label = tk.Label(text="is equal to")
    equal_label.grid(column=0, row=1)

    # output label
    output_label = tk.Label(text=0)
    output_label.grid(column=1, row=1)

    # km label
    km_label = tk.Label(text="km")
    km_label.grid(column=2, row=1)

    # calculate button
    calculate_button = tk.Button(text="Calculate", command=miles_to_km)
    calculate_button.grid(column=1, row=2)

    window.mainloop()