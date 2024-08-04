import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r"[\W_]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def check_password():
    password = password_entry.get()
    strength, feedback = assess_password_strength(password)

    result_label.config(text=f"Password Strength: {strength}")
    feedback_listbox.delete(0, tk.END)
    for item in feedback:
        feedback_listbox.insert(tk.END, item)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Enter your password:").grid(row=0, column=0, pady=5)
password_entry = tk.Entry(frame, show="*", width=30)
password_entry.grid(row=0, column=1, pady=5)

check_button = tk.Button(frame, text="Check Strength", command=check_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="Password Strength: ")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(frame, text="Feedback:").grid(row=3, column=0, pady=5)
feedback_listbox = tk.Listbox(frame, width=50, height=5)
feedback_listbox.grid(row=3, column=1, pady=5)

# Start the main event loop
root.mainloop()
