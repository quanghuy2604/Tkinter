from tkinter import *
from tkinter import messagebox


window = Tk()

window.title("Welcome App")

window.geometry('280x50')

lbl = Label(window, text="Input your Name:  ")

lbl.grid(column=0, row=0)

txt = Entry(window, width=20)

txt.grid(column=1, row=0)


def clicked():
    messagebox.showinfo('Message title', 'Welcome to Tkinter, '+ txt.get())

btn = Button(window, text="Accept", command=clicked)

btn.grid(column=1, row=1)

window.mainloop()
