from tkinter import *
from tkinter.ttk import *
import random

import tktoolbox.window

mGui = Tk()

mGui.geometry('450x450+500+300')
mGui.title('Grid Indexes')

for i in range(20):
    for j in range(20):
        if random.randint(1,10)<=2:
            continue
        mlabel = Label(text='{},{}'.format(i,j),
                )
        mlabel.grid(row=i,column=j,sticky=W)


tktoolbox.window.raise_by_thread(mGui)
# mGui.after(100, tktoolbox.window.focus)
mGui.mainloop()
