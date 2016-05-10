import time
from tkinter import *
def change_color(canvas, ov, color):
    color = 'yellow' if  (color != 'yellow') else 'blue'
    print("color =", color)
    canvas.itemconfig(ov, fill=color)
    canvas.update_idletasks()
    canvas.after(1500, change_color, canvas, ov, color)
root = Tk()
root.title('Canvas')
canvas = Canvas(root, width=200, height=200)
color = 'yellow'
ov=canvas.create_oval(10,10,50,50, fill=color)
canvas.pack()
change_color(canvas, ov, color)
root.mainloop()
