'''
from time import *
import os
from random import *
import tkinter as tk
from PIL import Image, ImageTk

def update_one_image(mode, ridx, cidx, repeat):
    rand_card_index = 0
    INDEX_MAX = 36
    image_folder = "Game_24_Images\\easy_cards\\"

    if mode == "hard":
      image_folder = "Game_24_Images\\hard_cards\\"
      INDEX_MAX = 42

    for i in range(60):
      rand_card_index  = randint(1, INDEX_MAX)
      images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
      image_path = images[rand_card_index - 1]
      global image
      image = Image.open(image_path)
      image = image.resize((250, 250))
      global photo
      photo = ImageTk.PhotoImage(image)
      global image_label
      global root
      image_label= tk.Label(root, image=photo)
      image_label.grid(row=ridx, column=cidx)
      sleep(0.05)
    return 1

if __name__ == "__main__":
    root = tk.Tk()
    update_one_image("hard", 0, 0, 1)
'''
import tkinter as tk

def on_enter_pressed(event):
    print("Enter key pressed!")

root = tk.Tk()
root.title("Enter Key Example")

root.bind('<Return>', on_enter_pressed)
root.bind('<KP_Enter>', on_enter_pressed)

label = tk.Label(root, text="")
label.pack(pady=100)

root.mainloop()
