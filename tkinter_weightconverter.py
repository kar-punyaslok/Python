from tkinter import *

window = Tk()


def kg_converter():
    pounds = float(e1_value.get())*2.2
    ounces = float(e1_value.get())*35.274
    grams = float(e1_value.get())*1000
    t1.insert(END, pounds)
    t2.insert(END, ounces)
    t3.insert(END, grams)


l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=kg_converter)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=10)  # 1, 10 are cell spans
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=10)  # 1, 10 are cell spans
t2.grid(row=1, column=1)


t3 = Text(window, height=1, width=10)  # 1, 10 are cell spans
t3.grid(row=1, column=2)


window.mainloop()
