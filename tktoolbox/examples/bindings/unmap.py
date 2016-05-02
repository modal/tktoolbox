""" http://stackoverflow.com/a/3840216/170656

For example, run the following code and then minimize the main window. The
tool window should disappear when the main window is minimized.

"""
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        tk.Label(self.root, text="main window").pack()
        self.t = tk.Toplevel()
        tk.Label(self.t, text="tool window").pack()
        self.root.bind("<Unmap>", self.OnUnmap)
        self.root.bind("<Map>", self.OnMap)
        self.root.mainloop()

    def OnMap(self, event):
        # show the tool window
        self.t.wm_deiconify()

    def OnUnmap(self, event):
        # withdraw the tool window
        self.t.wm_withdraw()

if __name__ == "__main__":
    app=App()
