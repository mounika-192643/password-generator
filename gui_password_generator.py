import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.resizable(False, False)

# Title
title_label = tk.Label(window, text="Secure Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Length input
length_frame = tk.Frame(window)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side=tk.LEFT)

# Options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

options_frame = tk.Frame(window)
options_frame.pack(pady=5)

tk.Checkbutton(options_frame, text="Uppercase Letters", variable=var_upper).pack(anchor='w')
tk.Checkbutton(options_frame, text="Lowercase Letters", variable=var_lower).pack(anchor='w')
tk.Checkbutton(options_frame, text="Digits", variable=var_digits).pack(anchor='w')
tk.Checkbutton(options_frame, text="Symbols", variable=var_symbols).pack(anchor='w')

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display password
password_display = tk.Entry(window, font=("Arial", 12), width=30, justify='center')
password_display.pack(pady=10)

# Run the app
window.mainloop()
