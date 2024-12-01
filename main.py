import tkinter as tk

# Function to handle counter operations
def update_counter(operation):
    global counter
    if operation == "increment":
        counter += 1
    elif operation == "decrement":
        counter -= 1
    elif operation == "reset":
        counter = 0

    # Update the label with the new counter value
    counter_label.config(text=f"Counter: {counter}")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Counter Application")
root.geometry("300x200")

# Initialize the counter variable
counter = 0

# Create the GUI widgets
counter_label = tk.Label(root, text=f"Counter: {counter}", font=("Arial", 16))
increment_button = tk.Button(root, text="Increment", command=lambda: update_counter("increment"))
decrement_button = tk.Button(root, text="Decrement", command=lambda: update_counter("decrement"))
reset_button = tk.Button(root, text="Reset", command=lambda: update_counter("reset"))

# Place the widgets on the window
counter_label.pack(pady=20)
increment_button.pack(side=tk.LEFT, padx=20)
decrement_button.pack(side=tk.LEFT, padx=20)
reset_button.pack(side=tk.LEFT, padx=20)

# Run the application
root.mainloop()
