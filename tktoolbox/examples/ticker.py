''' Tk_Text_ticker102.py
using Tkinter to create a marquee/ticker
uses a display width of 20 characters
not superbly smooth but good enough to read
tested with Python27 and Python33  by  vegaseat  04oct2013
'''
import time
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
root = tk.Tk()
# width --> width in chars, height --> lines of text
text_width = 20
text = tk.Text(root, width=text_width, height=1, bg='yellow')
text.pack()
# use a proportional font to handle spaces correctly
text.config(font=('courier', 48, 'bold'))
s1 = "We don't really care why the chicken crossed the road.  "
s2 = "We just want to know if the chicken is on our side of the "
s3 = "road or not. The chicken is either for us or against us.  "
s4 = "There is no middle ground here.  (George W. Bush)"
# pad front and end of text with spaces
s5 = ' ' * text_width
# concatenate it all
s = s5 + s1 + s2 + s3 + s4 + s5
for k in range(len(s)):
    # use string slicing to do the trick
    ticker_text = s[k:k+text_width]
    text.insert("1.1", ticker_text)
    root.update()
    # delay by 0.22 seconds
    time.sleep(0.22)
root.mainloop()
