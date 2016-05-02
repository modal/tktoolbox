""" http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm """
from tkinter import *
import tkinter.messagebox as msgbox


def callback():
    if msgbox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

root = Tk()
root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()
