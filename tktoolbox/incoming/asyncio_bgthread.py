import asyncio
from tkinter import *
from math import *

@asyncio.coroutine
def greet_every_two_seconds():
    while True:
        print('Hello World')
        yield from asyncio.sleep(2)

def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(greet_every_two_seconds())

loop = asyncio.get_event_loop()
import threading
t = threading.Thread(target=loop_in_thread, args=(loop,), daemon=True)
t.start()

###############

def evaluate(event):
    res.configure(text="Ergebnis: " + str(eval(entry.get())))

w = Tk()
Label(w, text="Your Expression:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()

def cmd():
    async def f():
        for i in range(10):
            print('sent! {}'.format(i))
            await asyncio.sleep(0.5, loop=loop)
    asyncio.run_coroutine_threadsafe(f(), loop)

Button(w, text='Send', command=cmd).pack()

async def ui():
    while True:
        w.update_idletasks()
        await asyncio.sleep(1/60)

w.mainloop()
