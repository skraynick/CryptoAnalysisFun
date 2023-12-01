import tkinter as tk
from tkinter import ttk, LEFT, RIGHT, BOTTOM, DISABLED

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.LetterCounter import get_frequencies

# TODO create a proper layout.
root = tk.Tk()

window_width = 800
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.title("Frequency Analysis Tool!")
root.minsize(window_width, window_height)

# Entry frame
frame = tk.Frame(root)
frame.pack()

mylabel = tk.Label(frame, text='Enter your Crypto text:')
mylabel.pack(side=LEFT)

# bar graph frame - for graph and options. sits below input field
working_frame = tk.Frame(root)
working_frame.pack()

# left options panel - TODO
#options_label = tk.Label(working_frame, text="Analysis Options: ")
#options_label.pack(side=LEFT)

# creating the bar plot
fig = plt.figure(figsize=(10, 5))
plt.bar(0, 0, color='pink',
        width=0.4)

plt.xlabel("Letters in Crytoptext")
plt.ylabel("Frequency of Letters")
plt.title("Frequency bar graph.")

canvas = FigureCanvasTkAgg(fig, master=working_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=LEFT)

# create the Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas,
                               working_frame)
toolbar.update()

# Get values from entry field.
cryptotext = tk.StringVar()
cryptotext_entry = ttk.Entry(
    frame,
    textvariable=cryptotext
)
cryptotext_entry.pack(side=LEFT)
# using lambda
cryptotext_entry.bind("<Return>", (lambda event: cryptotext_entered()))


# get cryptotext
def cryptotext_entered():
    plt.cla()
    plt.bar(list(get_frequencies(cryptotext.get().upper()).keys()),
            list(get_frequencies(cryptotext.get().upper()).values()), color='purple',
            width=0.4)
    canvas.draw()


enter_button = tk.Button(frame, text="Enter!", command=lambda: cryptotext_entered())
enter_button.pack(side=LEFT)



root.mainloop()
