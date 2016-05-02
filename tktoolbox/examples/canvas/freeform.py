from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack(fill=BOTH)

square = canvas.create_rectangle(0,0,150,150, fill="green")

root.mainloop()
