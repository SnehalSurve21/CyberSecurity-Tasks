import tkinter as tk
from tkinter import messagebox

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    result.set(f"Encrypted text: {cipher_text}")

def decryption(cipher_text, shift_key): 
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    result.set(f"Decrypted text: {plain_text}")

def perform_operation():
    text = message.get().lower()
    try:
        key = int(shift_key.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift key must be a number")
        return

    if operation.get() == 'encrypt':
        encryption(plain_text=text, shift_key=key)
    elif operation.get() == 'decrypt':
        decryption(cipher_text=text, shift_key=key)
    else:
        messagebox.showerror("Invalid Operation", "Please select an operation")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place the widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Enter your message:").grid(row=0, column=0, pady=5)
message = tk.StringVar()
tk.Entry(frame, textvariable=message, width=50).grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter shift key:").grid(row=1, column=0, pady=5)
shift_key = tk.StringVar()
tk.Entry(frame, textvariable=shift_key, width=10).grid(row=1, column=1, pady=5, sticky="w")

operation = tk.StringVar(value='encrypt')
tk.Radiobutton(frame, text="Encrypt", variable=operation, value='encrypt').grid(row=2, column=0, pady=5)
tk.Radiobutton(frame, text="Decrypt", variable=operation, value='decrypt').grid(row=2, column=1, pady=5, sticky="w")

tk.Button(frame, text="Submit", command=perform_operation).grid(row=3, column=0, columnspan=2, pady=10)

result = tk.StringVar()
tk.Label(frame, textvariable=result).grid(row=4, column=0, columnspan=2, pady=5)

# Start the main event loop
root.mainloop()
