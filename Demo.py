from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
from datetime import timedelta
import datetime

window = Tk()
now_date = datetime.datetime.now()

window.title("Welcome App")

window.geometry('380x90')
#Row1
lbl = Label(window, text="   Input your Name:  ")
lbl.grid(column=0, row=0)

txt = Entry(window, width=20)
txt.grid(column=1, row=0)
#Row2
lb_date = Label(window, text ="Input your birth: ")
lb_date.grid(column=0, row=2)

cal = DateEntry(font="Arial 14",year=1999,date_pattern='dd/mm/y')
cal.grid(column=1,row=2)

def clicked():
    delta = abs(now_date.date() - cal.get_date())
    messagebox.showinfo('Message title', 'Welcome to Tkinter, ' + txt.get())
    if now_date.date() != cal.get_date():
        messagebox.showinfo('Message title', ' You lived in this world ' + str(delta))
    else:
        messagebox.showinfo('Message title', 'Welcome to the World, You lived in this world ')


btn = Button(window, text="Accept", command=clicked)
btn.grid(column=1, row=3)

window.mainloop()
