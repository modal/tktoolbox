""" http://www.python-course.eu/tkinter_layout_management.php """
from tkinter import *
root = Tk()
root.title("python")
root.geometry("400x400")

label1 = Label(root, text="Type a thing:")
entry1 = Entry(root)

button_1 = Button(root, text="Sign In", command=lambda: print('hi!'))

label1.grid(row=1, column=0, padx=(0,15))
entry1.grid(row=1, column=1)
button_1.grid(row=2, sticky=W)

root.mainloop()
