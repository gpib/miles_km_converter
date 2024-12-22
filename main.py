import tkinter

def calculate():
    if my_label.cget("text") == "Miles":
        my_label_result.config(text = float(input.get())*1.609344)
    else:
        my_label_result.config(text=float(input.get()) * 0.621371192)


def switch():
    # Zamiana tekstów etykiet
    if my_label.cget("text") == "Miles":
        my_label.config(text="Km")
        my_label_2.config(text="Miles")
    else:
        my_label.config(text="Miles")
        my_label_2.config(text="Km")

window = tkinter.Tk()
window.title("Miles kilometers converter")
window.minsize(width=500, height=500)
window.config(padx = 20, pady = 20)

input = tkinter.Entry(width = 10)
input.grid(column = 1, row = 0)

my_label = tkinter.Label(text ="Miles")
my_label.grid(column = 2, row = 0)
my_label.config(padx = 5, pady = 5)

my_label_equal = tkinter.Label(text ="is equal to")
my_label_equal.grid(column = 0, row = 1)
my_label_equal.config(padx = 5, pady = 5)

my_label_result = tkinter.Label(text ="")
my_label_result.grid(column = 1, row = 1)
my_label_result.config(padx = 5, pady = 5)

my_label_2 = tkinter.Label(text ="Km")
my_label_2.grid(column = 2, row = 1)
my_label_2.config(padx = 5, pady = 5)

button = tkinter.Button(text = "Calculate", command = calculate)
#button.pack()
button.grid(column = 1, row = 2)
button.config(padx = 5, pady = 5)

button_switch = tkinter.Button(text = "Switch", command = switch)
#button.pack()
button_switch.grid(column = 2, row = 2)
button_switch.config(padx = 5, pady = 5)

window.mainloop()