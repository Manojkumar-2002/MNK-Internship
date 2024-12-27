from tkinter import  *

from bokeh.layouts import column
from django.forms.widgets import Input
from mpmath.matrices.matrices import rowsep

screen = Tk()
screen.title("Hero")
screen.geometry("400x400")


def printer():
    user_inp = inp.get()
    label.config(text = user_inp)


label = Label(screen,text="Hii", font=("Arial", 16))
label.grid(row=0,column=0)

inp = Entry(screen,width=20)
inp.grid(row=0,column=2)


button = Button(screen,text="btn",command=printer)
button.grid(row=1,column=1)



screen.mainloop()