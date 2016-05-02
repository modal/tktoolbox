import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()

# Create named fonts, reading the current defaults
# (thus if users use option database files, this honors their settings).
mainFontDescr = tk.Button()["font"]  # same as Label, Checkbutton, Menu...
entryFontDescr = tk.Entry()["font"]  # same as Text
mainFont = tkFont.Font(font=mainFontDescr)
entryFont = tkFont.Font(font=entryFontDescr)
# Set the option database; be sure to set the more general options first.
root.option_add("*Font", mainFont)
root.option_add("*Entry*Font", entryFont)
root.option_add("*Text*Font", entryFont)

# This is a quick and dirty demo of live font update
tk.Label(root, text="Test Label").pack()
fontList = tkFont.families()
entryVar = tk.StringVar()
entryVar.set(mainFont.cget("family"))


def setMainFont(varName, *args):
    mainFont.configure(family=root.globalgetvar(varName))


entryVar.trace_variable("w", setMainFont)
mainMenu = tk.OptionMenu(root, entryVar, *fontList)
mainMenu.pack()
root.mainloop()
