from tkinter import *
from tkinter.ttk import *
import random

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


mGui.mainloop()
