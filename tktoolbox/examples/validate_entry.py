'''
Info by Fredrik Lundh:
This module implements a validating version of the Tkinter Entry widget.
It uses the textvariable option to attach a StringVar to the widget,
and uses the variable trace function to keep track of what's going on (in real time, as the user types the input).
To specify how validation is to be done, override the validate method.
Note that the constructor takes a parent widget, and also allows you to use the value option to specify the initial contents.
All other options are passed on to the Entry widget itself.
'''

from tkinter import *


class ValidatingEntry(Entry):
    # base class for validating entry widgets

    def __init__(self, master, value="", **kw):
        Entry.__init__(self, master, **kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(value)
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)
        self.results = StringVar()
        if self.__value is None:
            self.results.set(None)
        else:
            self.results.set(self.__value)

    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(newvalue)
        else:
            self.__value = value

    def validate(self, value):
        # override: return value, new value, or None if invalid
        self.results.set(value)
        return value

    def getresults(self, value):
        # override: return value, or chopped value in the case of ChopLengthEntry
        return self.results.get()


'''
The first two examples are subclasses that check that the input is a valid Python integer or float, respectively.
The validate method simply tries to convert the value to an object of the right kind, and returns None (reject) if that fails.
'''


class IntegerEntry(ValidatingEntry):
    def validate(self, value):
        try:
            if value:
                v = int(value)
                self.results.set(value)
            return value
        except ValueError:
            return None


class FloatEntry(ValidatingEntry):
    def validate(self, value):
        try:
            if value:
                v = float(value)
                self.results.set(value)
            return value
        except ValueError:
            return None


class MaxLengthEntry(ValidatingEntry):
    '''MaxLength is a subclass that restricts the length of the input to a given max length.
       The getresults method is provided only to deal with a situation where a too-long
       initial value is provided, and the user accepts it without editing.
       Also if a too-long initial value is provided, it must be truncated to at least one char
       less than the max length, or else the user will be unable to even edit it
       (since the Del or BS key would cause the length to exceed the maxlength, they would be ignored)'''

    def __init__(self, master, value="", maxlength=None, **kw):
        if len(value) > maxlength - 1:
            value = value[:maxlength - 1]
        self.maxlength = maxlength
        ValidatingEntry.__init__(self, master, value=value)

    def validate(self, value):
        if self.maxlength is None or len(value) <= self.maxlength:
            self.results.set(value)
            return value
        return None  # new value too long

    def getresults(self, value):
        if self.maxlength:
            if len(value) > self.maxlength:
                value = value[:self.maxlength]
                self.results.set(value)
        return self.results.get()


class ChopLengthEntry(ValidatingEntry):
    '''ChopLengthEntry accepts all entries, but chops them when the results are called for'''

    def __init__(self, master, value="", maxlength=None, **kw):
        self.maxlength = maxlength
        ValidatingEntry.__init__(self, master, value=value)

    def getresults(self, value):
        if self.maxlength:
            if len(value) > self.maxlength:
                value = value[:self.maxlength]
                self.results.set(value)
        return self.results.get()


class StringEntry(ValidatingEntry):
    # same as ValidatingEntry; nothing extra
    pass


if __name__ == '__main__':
    labelString = ['Integer', 'Float', 'String', 'MaxLength', 'ChopLength']
    limitString = ['MaxLength', 'ChopLength']
    initial = [123, 456.789, '"hello, world!"', '"long text"',
               '"Please don\'t cut me!"']
    num = len(labelString)

    entry = [None] * num;
    value = [None] * num


    def results():
        resultsList = []
        for i in range(num):
            value[i] = entry[i].results.get()
            value[i] = entry[i].getresults(value[i])
            if value[i] is not None:
                resultsList.append(value[i])
        for x, y in zip(labelString, resultsList):
            print("validated %s entry is: %s" % (x, y))
        root.destroy()


    root = Tk()
    lab = [];
    but = [];
    entry = []
    # if we put the names of the various widget into a list, we can create instances
    #  using a for loop. Note that we need to handle
    #  the special case that 2 of them have a 2nd argument, while the others don't
    # (alternatively, could have re-defined the widgets to all take a (sometimes unneeded) 2nd argument)
    for i in range(num):
        but.append(None)
        lab.append(Label(text='please enter a ' + labelString[i]))
        lab[-1].pack(side='top')
        if labelString[i] in limitString:
            entry.append(eval(labelString[i] + 'Entry')(root, value=initial[i],
                                                        maxlength=10))
        else:
            entry.append(eval(labelString[i] + 'Entry')(root, value=initial[i]))
        entry[-1].pack()

    bt = Button(text='Ok', command=results)
    bt.pack(side='left')
    cn = Button(text='Cancel', command=root.destroy)
    cn.pack(side='left')
    mainloop()
