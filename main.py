from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

my_label = Label(text="Label", font=("Arial", 22))
my_label.grid(row=0,column=0)
my_label["text"] = "new text"
my_label.config(text="new text2")
my_label.config(padx=20,pady=20)


def button_clicked():
    #my_label.config(text="button clicked")
    my_label.config(text=input_box.get())


button = Button(text="Submit", command=button_clicked)
button.grid(row=1,column=1)

button2 = Button(text="Cancel", command=button_clicked)
button2.grid(row=0,column=3)

input_box = Entry(width=10)
input_box.grid(row=2,column=4)


# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 3, 5))

window.mainloop()
