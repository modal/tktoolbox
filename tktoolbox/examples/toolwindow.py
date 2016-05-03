# show Toplevel in ToolWindow style
from tkinter import *

root = Tk()
root.lower()
child = Toplevel(root)
# strange call format for wm_attributes(self, *args)
# ('-alpha',double, '-disabled',bool, '-toolwindow',bool, '-topmost',bool)
print(child.wm_attributes())  # defaults
# child.wm_attributes('-alpha', 1.0, '-disabled', 0, '-toolwindow', 1)
child.wm_attributes('-alpha', 1.0, )

root.mainloop()
