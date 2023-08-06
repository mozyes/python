from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.minsize(240, 110)
windows.config(padx=20, pady=20)

user_data = Entry(width=15)
user_data.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)


def button_clicked():
    miles = float(user_data.get())
    km = round(1.60934 * miles, 2)
    output_label.config(text=km)


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)

windows.mainloop()
