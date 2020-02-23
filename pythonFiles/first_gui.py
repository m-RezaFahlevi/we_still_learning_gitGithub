import tkinter
from tkinter import ttk

win = tkinter.Tk()

win.title("Python Graphical User Interfaces")
_label = ttk.Label(win, text="A Label")
_label.grid(column=0, row=0)

def __st_action_onclick__():
    st_action.configure(text="** I have been clicked! **")
    _label.configure(foreground='red')
    _label.configure(text='A Red Label')

def __nd_action_onclick__():
    nd_action.configure(text="** I have been clicked! **")
    _label.configure(foreground='green')
    _label.configure(text='A green Label')

def __thrd_action_onclick__():
    thrd_action.configure(text="** I have been clicked! **")
    _label.configure(foreground='yellow', background='blue')
    _label.configure(text='A Yellow Label')

def __fourth_action_onclick__():
    fourth_action.configure(text="** I have been clicked! **")
    _label.configure(foreground='blue', background='black')
    _label.configure(text="A blue Label")

st_action = ttk.Button(win, text="Click Me!", command=__st_action_onclick__)
st_action.grid(column=1, row=0)

nd_action = ttk.Button(win, text="Click Me!", command=__nd_action_onclick__)
nd_action.grid(column=2, row=0)

thrd_action = ttk.Button(win, text="Click Me!", command=__thrd_action_onclick__)
thrd_action.grid(column=3, row=0)

fourth_action = ttk.Button(win, text="Click Me!", command=__fourth_action_onclick__)
fourth_action.grid(column=4, row=0)

win.mainloop()
