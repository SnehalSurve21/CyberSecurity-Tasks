import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import numpy as np

window = tk.Tk()
window.geometry("1000x700")
window.title("Image Encryption Decryption")

global panelA, panelB, image_encrypted, key, image_path
panelA = None
panelB = None
image_encrypted = None
key = None
image_path = None

def openfilename():
    return filedialog.askopenfilename(title='Open', filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

def open_img():
    global image_path, panelA, panelB
    image_path = openfilename()
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)

        if panelA is None or panelB is None:
            panelA = tk.Label(image=img)
            panelA.image = img
            panelA.pack(side="left", padx=10, pady=10)
            panelB = tk.Label(image=img)
            panelB.image = img
            panelB.pack(side="right", padx=10, pady=10)
        else:
            panelA.configure(image=img)
            panelB.configure(image=img)
            panelA.image = img
            panelB.image = img
    else:
        messagebox.showwarning("Warning", "No image selected.")

def en_fun(image_path):
    global image_encrypted, key
    if image_path is not None:
        image_input = Image.open(image_path).convert("RGB")
        image_array = np.array(image_input)

        # Create a random key
        key = np.random.randint(0, 256, image_array.shape, dtype=np.uint8)

        # XOR encryption
        image_encrypted = np.bitwise_xor(image_array, key)

        # Save and display the encrypted image
        encrypted_image = Image.fromarray(image_encrypted)
        encrypted_image.save('image_encrypted.png')

        img = Image.open('image_encrypted.png')
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        panelB.configure(image=img)
        panelB.image = img

        messagebox.showinfo("Encrypt Status", "Image Encrypted successfully.")
        save_file('image_encrypted.png')
    else:
        messagebox.showwarning("Warning", "No image selected.")

def de_fun():
    global image_encrypted, key
    if image_encrypted is not None and key is not None:
        # XOR decryption
        image_decrypted = np.bitwise_xor(image_encrypted, key)

        # Save and display the decrypted image
        decrypted_image = Image.fromarray(image_decrypted)
        decrypted_image.save('image_decrypted.png')

        img = Image.open('image_decrypted.png')
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        panelB.configure(image=img)
        panelB.image = img

        messagebox.showinfo("Decrypt Status", "Image Decrypted successfully.")
        save_file('image_decrypted.png')
    else:
        messagebox.showwarning("Warning", "Image not encrypted yet.")

def save_file(file_path):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
    if save_path:
        os.rename(file_path, save_path)
        messagebox.showinfo("Success", f"Image saved successfully at {save_path}")

def reset():
    global image_path, panelA, panelB
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        panelB.configure(image=img)
        panelB.image = img
        messagebox.showinfo("Success", "Image reset to original.")
    else:
        messagebox.showwarning("Warning", "No image selected.")

# UI Components
start1 = tk.Label(text="Image Encryption\nDecryption", font=("Arial", 40), fg="magenta")
start1.place(x=350, y=10)

start1 = tk.Label(text="Original\nImage", font=("Arial", 40), fg="magenta")
start1.place(x=100, y=270)

start1 = tk.Label(text="Encrypted\nDecrypted\nImage", font=("Arial", 40), fg="magenta")
start1.place(x=700, y=230)

chooseb = tk.Button(window, text="Choose", command=open_img, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
chooseb.place(x=30, y=20)

enb = tk.Button(window, text="Encrypt", command=lambda: en_fun(image_path), font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
enb.place(x=150, y=620)

deb = tk.Button(window, text="Decrypt", command=de_fun, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
deb.place(x=450, y=620)

resetb = tk.Button(window, text="Reset", command=reset, font=("Arial", 20), bg="yellow", fg="blue", borderwidth=3, relief="raised")
resetb.place(x=800, y=620)

def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = tk.Button(window, text="EXIT", command=exit_win, font=("Arial", 20), bg="red", fg="blue", borderwidth=3, relief="raised")
exitb.place(x=880, y=20)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
