from tkinter import *

windows = Tk()
windows.minsize(500,300)

first_label = Label(text="Click me")
first_label.pack()

def button_clicked():
    first_label.config(text="I got clicked")


button = Button(text="Click me", command=button_clicked)
button.pack()

windows.mainloop()
