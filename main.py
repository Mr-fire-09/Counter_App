import tkinter as tk
from tkinter import ttk

# Function to update the counter value
def update_counter(operation):
    global counter
    if operation == "increment":
        counter += 1
    elif operation == "decrement":
        counter -= 1
    elif operation == "reset":
        counter = 0

    counter_label.config(text=f"{counter}")


# Initialize the main application window
root = tk.Tk()
root.title("Modern Counter App")
root.geometry("400x400")
root.configure(bg="#003366")  # Background color

# Counter value
counter = 0

# Styles
button_style = {
    "font": ("Arial", 18, "bold"),
    "bg": "#007BFF",
    "fg": "white",
    "relief": "flat",
    "width": 5,
}
label_style = {
    "font": ("Arial", 48, "bold"),
    "bg": "#003366",
    "fg": "white",
}

# Counter display
counter_label = tk.Label(root, text=f"{counter}", **label_style)
counter_label.pack(pady=40)

# Decrement button
decrement_button = tk.Button(root, text="-", command=lambda: update_counter("decrement"), **button_style)
decrement_button.place(x=50, y=200)

# Increment button
increment_button = tk.Button(root, text="+", command=lambda: update_counter("increment"), **button_style)
increment_button.place(x=300, y=200)

# Reset button
reset_button = tk.Button(root, text="Reset", command=lambda: update_counter("reset"), **button_style)
reset_button.pack(side=tk.BOTTOM, pady=30)

# Run the application
root.mainloop()
