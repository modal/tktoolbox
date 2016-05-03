""" http://python.6.x6.nabble.com/Difficulty-getting-started-with-a-BWidget-Tree-td1973565.html """
import tkinter as tk
import bwidget as bw
import os

class DirTree(tk.Frame):
    def __init__(self, master, *args, **kw):
        tk.Frame.__init__(self, master)
        self.tree = tree = bw.Tree(self, opencmd=self.open_folder, closecmd=self.close_folder, *args, **kw)
        tree.pack(fill='both', expand=1)

        self.folder_icon = tk.PhotoImage(file='/usr/share/pybwidget/images/folder.gif')
        self.openfolder_icon = tk.PhotoImage(file='/usr/share/pybwidget/images/openfold.gif')
        self.file_icon = tk.PhotoImage(file='/usr/share/pybwidget/images/file.gif')

        node = self.tree.insert('end', 'root', text='/', image=self.folder_icon, drawcross='allways', data='/')
        self.tree.opentree(node, recurse=0)

    def close_folder(self, node):
        self.tree.itemconfigure(node, image=self.folder_icon)

    def open_folder(self, node):
        path = self.tree.itemcget(node, 'data')
        children = os.listdir(path)
        files, dirs = [], []
        for item in children:
            if os.path.isdir(os.path.join(path, item)):
                dirs.append(item)
            #else:
            #    files.append(item)
        dirs.sort()
        #files.sort()
        for item in dirs:
            newpath = os.path.join(path, item)
            self.tree.insert('end', node, text=item, image=self.folder_icon, drawcross='allways', data=newpath)
        #for item in files:
        #    newpath = os.path.join(path, item)
         #   self.tree.insert('end', node, text=item, image=self.file_icon, drawcross='never', data=newpath)
        self.tree.itemconfigure(node, image=self.openfolder_icon)


def test():
    r = tk.Tk()
    t = DirTree(r, bg='white', selectbackground='blue4', selectforeground='white', deltax=18, deltay=18)
    t.pack(fill='both', expand=1)
    r.mainloop()

if __name__== '__main__':
    test()
