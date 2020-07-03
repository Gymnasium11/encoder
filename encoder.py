import os
import ctypes
from tkinter import *
import tkinter.ttk as ttk

# window settings

root = Tk()
root.resizable(width=False, height=False)
root.geometry('770x500')
root.title('Шифратор 2.0')

# icons

if os.name == 'nt':
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap('encode2.ico')

# RadioButtons

a = IntVar()
a.get()

rb1 = ttk.Radiobutton(root, text='Шифр Цезаря', variable=a, value=5)
rb2 = ttk.Radiobutton(root, text='Шифр Виженера', variable=a, value=10)
rb3 = ttk.Radiobutton(root, text='Шифр Бабугана', variable=a, value=15)
rb1.grid(row=0, column=0, padx="15 0", pady="30 0")
rb2.grid(row=0, column=1, padx="20 0", pady="30 0")
rb3.grid(row=0, column=2, padx="25 0", pady="30 0")


def selected(self):
    if my_var.get() == 5:
        "do something"
    elif my_var.get() == 10:
        "do something"
    else:
        "do something"


# Entries and Texts

input = Text(width=36, height=20).grid(row=1, column=0, padx="10 0", pady="40 0")
output = Text(width=36, height=20).grid(row=1, column=2, padx="21 0", pady="40 0")
key = Text(width=7, font="helvetica 22 bold", height=1).grid(row=1, column=1, pady="100 0", padx="14 0")

# Buttons

ttk.Button(text='Зашифровать', width=19).grid(row=1, column=1, padx="20 0", pady="0 190")
ttk.Button(text='Расшифровать', width=19).grid(row=1, column=1, padx="20 0", pady="0 120")
ttk.Button(text='Вставить', width=19).grid(row=3, column=0, pady="30 0")
ttk.Button(text='Вставить', width=19).grid(row=3, column=2, sticky=W, pady="30 0", padx="30 0")
ttk.Button(text='Копировать', width=19).grid(row=3, column=2, padx="180 0", pady="30 0")

# Label

ttk.Label(root, text="Ключ", font='helvetica 20 bold').grid(row=1, column=1, padx="10 0")

root.mainloop()
