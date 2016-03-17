'''
  This file defines one function : show(texts), which is used to show the texts
  on a window.
'''
from Tkinter import *


def show(texts):
    '''
    Shows the texts on a window.
    '''

    master = Tk()
    master.title("Oliver")
    listbox = Listbox(master, height = 20, width = 100, font='Courier 10', fg='blue')
    scroll = Scrollbar(master, command=listbox.yview)
    listbox.configure(yscrollcommand=scroll.set)
    listbox.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)
    master.wm_resizable(False, False)
    for item in texts:
        listbox.insert(END, item)
    master.mainloop()
