from tkinter import *
from tkinter.scrolledtext import ScrolledText
from prime import click

window = Tk()
window.title('Prime Numbers Calculator')
window.configure(bg='black')
window.geometry('900x400')
window.grid_columnconfigure((0, 1), weight=1)
window.grid_rowconfigure((0,1,3,4,6), weight=1)
Label(window, text='Enter a positive number >= 2:', bg='black', fg='white', font='arial 12 bold')\
    .grid(row=0, column=0, sticky=W)
Label(window, text='Enter the high limit of the calculation:', bg='black', fg='white', font='arial 12 bold')\
    .grid(row=2, column=0, sticky=W)
numberentry = Entry(window, width=15, bg='white', font='arial 12')
numberentry.grid(row=0, column=1)
numberentrytwo = Entry(window, width=15, bg='white', font='arial 12')
numberentrytwo.grid(row=2, column=1)
primeout = ScrolledText(window, width=60, height=4, bg='white', font='arial 12')
primeout.grid(row=5, column=1, columnspan=2)
Label(window, text='Result:', bg='black', fg='white', font='arial 12 bold')\
    .grid(row=5, column=0, sticky=W)
button_command = lambda:[primeout.delete(0.0, END),\
    primeout.insert(0.0,click(numberentry.get(),numberentrytwo.get())),\
    numberentry.delete(0, END),\
    numberentrytwo.delete(0,END)] # single zero since it has 1 line of text
Button(window, text='Calculate', width=9, command=button_command, font='arial 12').grid(row=3, column=1)

window.resizable(0,0)
window.mainloop()