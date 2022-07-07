import tkinter as tk
from PIL import ImageTk, Image

def show_screen(screen):
    screen.tkraise()

root = tk.Tk()

root.state('zoomed')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


home_screen = tk.Frame(root)
recording_screen = tk.Frame(root)


for screen in (home_screen, recording_screen):
    screen.grid(row=0, column=0, sticky='nsew')

# home screen code

def start_recording():
    # move to recording screen
    show_screen(recording_screen)
    # start the microphone

app_name = tk.Label(home_screen, text='Easy Bible', padx=50, pady=50)
app_name.pack(fill="x")

play_icon = ImageTk.PhotoImage(Image.open('play.png'))
play_button = tk.Button(home_screen, image=play_icon, borderwidth=0, command=start_recording)
play_button.pack()

# recording screen code

def stop_recording():
    #  turn off the microphone 
    # go back to home screen
    show_screen(home_screen)

recording_indicator = tk.Label(recording_screen, text='detecting bible verses', padx=50, pady=50)
recording_indicator.pack(fill='x')

pause_icon = ImageTk.PhotoImage(Image.open('pause.png'))
pause_button = tk.Button(recording_screen, image=pause_icon, borderwidth=0, command=stop_recording)
pause_button.pack()

show_screen(home_screen)

root.mainloop()