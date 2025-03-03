import tkinter as tk

# Function to update the counter value
def update_counter(operation):
    global counter
    if operation == "increment":
        counter += 1
    elif operation == "decrement":
        counter -= 1
    elif operation == "reset":
        counter = 0

    # Trigger fade-out animation
    fade_out()

# Function to fade out the label
def fade_out():
    current_color = counter_label.cget("fg")
    if current_color == "#FFFFFF":  # If already white, skip fade-out
        fade_in()
        return

    r, g, b = root.winfo_rgb(current_color)
    r, g, b = r // 256, g // 256, b // 256  # Convert to 8-bit RGB

    # Gradually reduce opacity (fade to white)
    if r < 255 or g < 255 or b < 255:
        r = min(r + 15, 255)
        g = min(g + 15, 255)
        b = min(b + 15, 255)
        new_color = f"#{r:02x}{g:02x}{b:02x}"
        counter_label.config(fg=new_color)
        root.after(30, fade_out)  # Continue fading
    else:
        counter_label.config(text=f"{counter}")
        fade_in()  # Start fade-in after fade-out completes

# Function to fade in the label
def fade_in():
    current_color = counter_label.cget("fg")
    if current_color == "#FFFFFF":  # If already white, start fading to original color
        r, g, b = 255, 255, 255
    else:
        r, g, b = root.winfo_rgb(current_color)
        r, g, b = r // 256, g // 256, b // 256  # Convert to 8-bit RGB

    # Gradually increase opacity (fade to original color)
    if r > 0 or g > 0 or b > 0:
        r = max(r - 15, 0)
        g = max(g - 15, 0)
        b = max(b - 15, 0)
        new_color = f"#{r:02x}{g:02x}{b:02x}"
        counter_label.config(fg=new_color)
        root.after(30, fade_in)  # Continue fading
    else:
        counter_label.config(fg="white")  # Reset to original color

# Initialize the main application window
root = tk.Tk()
root.title("Modern Counter App with Animation")
root.geometry("600x600")  # Adjusted the window size
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
    "height": 2
}
label_style = {
    "font": ("Arial", 48, "bold"),
    "bg": "#003366",
    "fg": "white",  # Initial text color
}

# Counter display
counter_label = tk.Label(root, text=f"{counter}", **label_style)
counter_label.pack(pady=40)

# Create a frame to hold the buttons and make them fit the width
button_frame = tk.Frame(root, bg="#003366")
button_frame.pack(fill=tk.BOTH, expand=True)

# Decrement button
decrement_button = tk.Button(button_frame, text="-", command=lambda: update_counter("decrement"), **button_style)
decrement_button.pack(side=tk.LEFT, expand=True)

# Increment button
increment_button = tk.Button(button_frame, text="+", command=lambda: update_counter("increment"), **button_style)
increment_button.pack(side=tk.LEFT, expand=True)

# Reset button
reset_button = tk.Button(root, text="Reset", command=lambda: update_counter("reset"), **button_style)
reset_button.pack(side=tk.BOTTOM, pady=30, fill=tk.X)

# Run the application
root.mainloop()