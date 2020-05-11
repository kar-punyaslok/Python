from tkinter import *

window = Tk()


def km_to_miles():
    # We need .get() bc e1_value is not conventional python string
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)  # END=the text is entered at the end of row
    print(miles)


# We dont use () bc otherwise python would execute the method whenever it runs the script
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
# Entry is an area where user can input value
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# The output appears in Text
t1 = Text(window, height=1, width=10)  # 1, 10 are cell spans
t1.grid(row=0, column=2)

# This allows us to close at will
window.mainloop()
