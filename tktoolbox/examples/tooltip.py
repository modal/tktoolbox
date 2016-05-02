import tkinter as tk
from tktoolbox.tooltip import CreateToolTip

root = tk.Tk()
btn1 = tk.Button(root, text="button 1")
btn1.pack(padx=10, pady=5)
button1_ttp = CreateToolTip(btn1,
    'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, '
    'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
    'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam '
    'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.')

btn2 = tk.Button(root, text="button 2")
btn2.pack(padx=10, pady=5)
button2_ttp = CreateToolTip(btn2,
    "First thing's first, I'm the realest. Drop this and let the whole world "
    "feel it. And I'm still in the Murda Bizness. I could hold you down, like "
    "I'm givin' lessons in  physics. You should want a bad Vic like this.")

root.mainloop()
