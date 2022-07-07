from tkinter import *
from PIL import ImageTk, Image


root = Tk()

# 0
canvas = Canvas(root, width=1000, height=500)
canvas.grid(columnspan=3, rowspan=3)

# first_frame = LabelFrame(borderwidth=0)
# first_frame.grid(column=0, row=0, columnspan=3)

# add app label
# 1
app_label = Label(root, text='Easy Bible', pady=30)
app_label.grid(row=0, column=1)

def run():
    list = root.grid_slaves()
    list[0].destroy()
    pp()
    

def pp():
    pause_icon = ImageTk.PhotoImage(Image.open('pause.png'))
    pause_button = Button(root, image=pause_icon, borderwidth=0, command=run)
    pause_button.grid(row=2, column=1)

# add play button
# 2
play_icon = ImageTk.PhotoImage(Image.open('play.png'))
play_button = Button(root, image=play_icon, borderwidth=0, command=pp)
play_button.grid(row=1, column=1)

root.mainloop()