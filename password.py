import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        password_length = int(password_length_entry.get())
        if password_length < 8:
            raise ValueError("Password length should be at least 8 characters.")
        
        lowercase_chars = string.ascii_lowercase
        uppercase_chars = string.ascii_uppercase
        digit_chars = string.digits
        punctuation_chars = string.punctuation

        # Ensure at least one character from each category
        password_chars = [
            random.choice(lowercase_chars),
            random.choice(uppercase_chars),
            random.choice(digit_chars),
            random.choice(punctuation_chars)
        ]

        # Fill the rest of the password length with a random selection
        all_chars = lowercase_chars + uppercase_chars + digit_chars + punctuation_chars
        password_chars.extend(random.choices(all_chars, k=password_length-4))

        random.shuffle(password_chars)
        password = "".join(password_chars)
        
        generated_password.set(password)
    except ValueError as error:
        messagebox.showerror("Invalid Input", str(error))

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
password_length_label = tk.Label(root, text="Enter the length of the password:")
password_length_label.pack(pady=10)

password_length_entry = tk.Entry(root)
password_length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

generated_password = tk.StringVar()
password_result_label = tk.Label(root, textvariable=generated_password, font=("Helvetica", 12))
password_result_label.pack(pady=10)

# Run the application
root.mainloop()