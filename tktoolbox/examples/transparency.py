import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.count = 0
        b=tk.Button(text="create window", command=self.create_window)
        b.pack()
        self.root.mainloop()

    def create_window(self):
        self.count += 1
        t=FadeToplevel(self.root)
        t.wm_title("Window %s" % self.count)
        t.fade_in()


class FadeToplevel(tk.Toplevel):
    '''A toplevel widget with the ability to fade in'''
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.attributes("-alpha", 0.0)

    def fade_in(self):
        alpha = self.attributes("-alpha")
        alpha = min(alpha + .01, 1.0)
        self.attributes("-alpha", alpha)
        if alpha < 1.0:
            self.after(10, self.fade_in)

if __name__ == "__main__":
    app=App()
