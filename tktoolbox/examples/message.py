""" http://www.python-course.eu/tkinter_message_widget.php """

"""
The Options in Detail

anchor	The position, where the text should be placed in the message widget: N, NE, E, SE, S, SW, W, NW, or CENTER. The Default is CENTER.
aspect	Aspect ratio, given as the width/height relation in percent. The default is 150, which means that the message will be 50% wider than it is high. Note that if the width is explicitly set, this option is ignored.
background	The background color of the message widget. The default value is system specific.
bg	Short for background.
borderwidth	Border width. Default value is 2.
bd	Short for borderwidth.
cursor	Defines the kind of cursor to show when the mouse is moved over the message widget. By default the standard cursor is used.
font	Message font. The default value is system specific.
foreground	Text color. The default value is system specific.
fg	Same as foreground.
highlightbackground	Together with highlightcolor and highlightthickness, this option controls how to draw the highlight region.
highlightcolor	See highlightbackground.
highlightthickness	See highlightbackground.
justify	Defines how to align multiple lines of text. Use LEFT, RIGHT, or CENTER. Note that to position the text inside the widget, use the anchor option. Default is LEFT.
padx	Horizontal padding. Default is -1 (no padding).
pady	Vertical padding. Default is -1 (no padding).
relief	Border decoration. The default is FLAT. Other possible values are SUNKEN, RAISED, GROOVE, and RIDGE.
takefocus	If true, the widget accepts input focus. The default is false.
text	Message text. The widget inserts line breaks if necessary to get the requested aspect ratio. (text/Text)
textvariable	Associates a Tkinter variable with the message, which is usually a StringVar. If the variable is changed, the message text is updated.
width	Widget width given in character units. A suitable width based on the aspect setting is automatically chosen, if this option is not given.
"""
from tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
mainloop()
