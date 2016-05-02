""" http://www.python-course.eu/tkinter_layout_management.php """
from tkinter import *
from tkinter.ttk import Button
root = Tk()
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack()
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(ipadx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(ipady=10)
w = Button(root, text="Button")
w.pack(ipady=10)
mainloop()
