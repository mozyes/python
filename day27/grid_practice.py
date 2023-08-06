from tkinter import *

windows = Tk()
windows.title("My first GUI program!")
windows.minsize(500, 300)

my_label = Label(text="I am a label")
my_label.grid(column=0, row=0)

my_button = Button(text="Click Me")
my_button.grid(column=1, row=1)

my_entry = Entry(width=10)
my_entry.grid(column=3, row=2)

my_button_2 = Button(text="New Button")
my_button_2.grid(column=2, row=0)

windows.mainloop()
