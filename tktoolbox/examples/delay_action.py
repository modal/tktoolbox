# using the tk timer (Fredrik Lundh, June 1997)

from tkinter import *

root = Tk()

class App:

    def __init__(self, master):

        self.w = Button(root, text="Waiting", command=self.stop)
        self.w.pack()
        self.id = self.w.after(1000, self.timer)

    def timer(self):
        self.w.config(text=self.w["text"]+".")
        self.id = self.w.after(1000, self.timer)

    def stop(self):
        self.w.config(bg="gold")
        self.w.after_cancel(self.id)

app = App(root)

root.mainloop()
