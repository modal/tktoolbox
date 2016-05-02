import os
from tkinter import *

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

f = os.path.join(os.path.dirname(__file__), '../images/python.gif')

img = PhotoImage(file=f)
canvas.create_image(20,20, anchor=NW, image=img)

mainloop()
