import os
import threading
import time


def f():
    return 123


def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def focus():
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


def lift():
    time.sleep(0.1)
    with threading.Lock():
        focus()


def raise_by_thread(window):
    """ After a short delay, the application will be raised to the top. """
    thread = threading.Thread(target=lift, daemon=True)
    thread.start()
