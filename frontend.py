# %%
# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
from script import run_app

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")


def open_file():
    file = filedialog.askopenfile(mode='rb', filetypes=[('*.jpeg', '*.jpg')])
    print(type(file.name))
    print(file.name)
    # new_name = Path(file.name)
    new_path = f'"{file.name}"'
    print(new_path)
    im = Image.open(file)
    resized_image = im.resize((50, 50), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resized_image)
    myvar = Label(win, image=tkimage)
    myvar.image = tkimage
    myvar.pack()
    if file:
        content = file.read()
        file.close()
        print("%d characters in this file" % len(content))
    return new_path


# Add a Label widget
label = Label(win, text="Select the dog images", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button

browse_button = ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

generate_button = ttk.Button(win, text="Generate Breed", command=run_app(o)).pack(pady=20)

# generate_button = ttk.Button(win, text="Generate Breed", command= run_app(new_path)).pack(pady=20)

# generate_button = ttk.Button(win, text="Generate Breed", command=run_app()).pack(pady=20)

win.mainloop()

# %%
print("HELLO")

# %%
run_app(r"C:\Users\Alex Christopher\Downloads\goldenretriever.jpg")

# %%
run_app("E:/Mini Project/dog-human-classifier-neural-network/beagle.jpg")

# %%
run_app("beagle.jpg")

# %%
from matplotlib.image import imread

iimg = cv2.imread("3.jpg")
iimg

# %%
grayy = cv2.cvtColor(iimg, cv2.COLOR_BGR2GRAY)

grayy

# %%
run_app("E:/Mini Project/dog-human-classifier-neural-network/beagle.jpg")

# %%



