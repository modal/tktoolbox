from tkinter import *
"""
ButtonBar widget
Rick Lawson
r_b_lawson at yahoo dot com
Easy widget to mimic the ButtonBar which is showing up a lot in Windows
Inspired by Iuri Wickert's notebook.py widget (esp. the Radiobutton tricks)

config options
--------------
BusyBar is derived from frame so all frame options are fine
Here are the options specific to this widget
labels = sequence of button labels
images = sequence of PhotoImage objects
commands = sequence of commands to be executed when particular button is selected
"""
class ButtonBar(Frame):
    def __init__(self, master=None, **options):
        # make sure we have sane defaults
        self.master=master
        self.options=options
        self.labels = pop(options, 'labels')
        self.images = pop(options, 'images')
        self.commands = pop(options, 'commands')
        options.setdefault('bd', 2)
        options.setdefault('bg', 'white')
        options.setdefault('relief', GROOVE)
        self.tkVar = IntVar()

        # init the base class
        Frame.__init__(self, master, options)

        # load the images & create the buttons
        self.buttons = []
        index = 0
        for image in self.images:
            button = Radiobutton(self, indicatoron=0, text=self.labels[index], relief=FLAT, variable = self.tkVar, value=index, image=image, compound=TOP, bg='white', bd=0, pady=2, padx=2, command=self.commands[index], selectcolor='blue')
            button.bind('<Enter>', self._onEnter)
            button.bind('<Leave>', self._onLeave)
            button.pack()
            self.buttons.append(button)
            index += 1

    def getSelectedIndex(self):
        return self.tkVar.get()

    def _onEnter(self, event):
        b = event.widget
        b.config(bg='lightblue')

    def _onLeave(self, event):
        b = event.widget
        b.config(bg='white')

def pop(dict, key):
    value = dict[key]
    del dict[key]
    return value

if __name__=='__main__':
    root = Tk()

    #Done with imageEmbedder 1.0 utility img2pytk.py from
    #  http://www.3dartist.com/WP/python/pycode.htm#img2pytk
    img00 = PhotoImage(format='gif',data=
             'R0lGODlhGAAYAOb/AAAAAP///4GBl3FxgHJygH19hnx8g25uccvMUtfYW/Ly'
            +'AKurAP//Dbi4DdfXLcPDLsPEL+TkOsTFNNDQO8XGOsfIQcjJQtfXSdPUSeTk'
            +'UdXWUdbXVdbXVs3NVtDQYtHRY93dbODgeuHhgNbWfdbWfuPjh9jYhuTkj9ra'
            +'jerqperqp+rqqN7en9/fou3tsu3ts+PjsWZmUeXluOTkt2dnVfPzzXNzYXR0'
            +'Y2lpXff333d3be3t3e3t3nh4dGxsa7+bh8yolNnBs+bOwO3e1vrr49bDuuPQ'
            +'x8mxp6qOhLebkbyjmvLy8g0NDcDAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            +'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAE0A'
            +'LAAAAAAYABgAAAfwgE2Cg4SFhoeETACKigFLiIaLFy8tKSYRi4+QggAZMCos'
            +'KiglHiEOTJqQTDAuMjUEBSgiHRgAAZtMFyozOTsCAyskIBYNtpAALyw1PAE7'
            +'NSwnHhoQqKotKjK9AgQqwhUTxogAKSitr7GzGA/ViEwmJSigBgekHBLgt+IR'
            +'HiIjJz49PiSgMGEBO3EhOoD4oAPHBoLrUrVzgKHCDRo2Ykx4UCwfLgQTIGwc'
            +'GW5TEwARFIx8wMCgxE2LFjBQUOygySZMfjACkKTkTQBAghApcgSJTZM5hQwx'
            +'oqSnx5tLmAgl6vNmk6iLqlq96ujp1q9gNwUCACH+T0NvcHlyaWdodCAyMDAw'
            +'IGJ5IFN1biBNaWNyb3N5c3RlbXMsIEluYy4gQWxsIFJpZ2h0cyBSZXNlcnZl'
            +'ZC4NCkpMRiBHUiBWZXIgMS4wDQoAOw==')

    img01 = PhotoImage(format='gif',data=
             'R0lGODlhGAAYALP/AAAAAP///zAwYT09bpGRwp6ez8LC8s/P//Ly8g0NDcDA'
            +'wAAAAAAAAAAAAAAAAAAAACH5BAEAAAoALAAAAAAYABgAAASWUMlJq7134G1F'
            +'4qAyGF9IAQkqHEQZpocRx0X7ykSt5y2yJYadsPcL8lIJQS3hQzkDEwBriQgg'
            +'BkRFIkfyKaRHr8IjBtQOAKjWyKQMxFpu+ztNT5KU7dm+pkq2Gn88aGpfSHZ6'
            +'Hig8BV0TVpAIeoyMjhiTQzFzGJJcMzIocJxbB4opViYKkgZvkKkTkgKFr7Bv'
            +'tBZVt7oRACH+T0NvcHlyaWdodCAyMDAwIGJ5IFN1biBNaWNyb3N5c3RlbXMs'
            +'IEluYy4gQWxsIFJpZ2h0cyBSZXNlcnZlZC4NCkpMRiBHUiBWZXIgMS4wDQoA'
            +'Ow==')

    win = Frame(root, height=300, width=300)
    commands = [lambda w=win: w.config(bg='blue'), lambda w=win: w.config(bg='red')]
    bb = ButtonBar(root, labels=['Command 1', 'Command 2'], images=[img00, img01], commands=commands)
    bb.grid(row=0, column=0, sticky=NS)
    win.grid(row=0, column=1, sticky=NSEW)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=0)
    root.columnconfigure(1, weight=1)
    root.mainloop()
