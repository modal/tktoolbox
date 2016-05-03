""" http://stackoverflow.com/a/10423793/170656 """
# Fast
from tkinter import *
root = Tk()
label = Label(root)
label.pack()
img = PhotoImage(width=300,height=300)
data = ("{red red red red blue blue blue blue}")
img.put(data, to=(20,20,280,280))
label.config(image=img)
root.mainloop()
