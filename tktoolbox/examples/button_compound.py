from tkinter import *

root=Tk()
for comp in ("bottom", "center", "left", "none", "right", "top"):
    b = Button(root, compound=comp, text=comp, bitmap="error")
    b.pack()
root.mainloop()
