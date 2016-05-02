from tkinter import *
from tkinter.ttk import Button
from tkinter.filedialog import askopenfilename


def callback():
    name= askopenfilename()
    print(name)


errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X, padx=50, pady=50, ipady=10)
mainloop()
