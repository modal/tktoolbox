import tkinter
from random  import randint
from binascii import  hexlify
class App:
    def __init__(self, t, w=800, h=600):
        self.image = tkinter.PhotoImage(width=w, height=h)  # create empty image
        lines = []
        for _ in range(h):
            line = []
            for _ in range(w):
                rgb = [randint(0, 255) for _ in range(3)]
                line.append("#{:02x}{:02x}{:02x}".format(*rgb))
            lines.append('{{{}}}'.format(' '.join(line)))
        self.image.put(' '.join(lines))
        c = tkinter.Canvas(t, width=w, height=h);
        c.create_image(0, 0, image=self.image, anchor=tkinter.NW)
        c.pack()
t = tkinter.Tk()
a = App(t)
t.mainloop()
