import tkinter as tk
import random

def roll():
    # Unicode characters for dice faces
    dice_faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.config(text=random.choice(dice_faces))

root = tk.Tk()
root.title("Dice Simulator")
root.geometry("200x200")

label = tk.Label(root, text="", font=("Times", 100))
label.pack()

button = tk.Button(root, text="Roll Dice", command=roll)
button.pack(pady=20)

root.mainloop()
 
 