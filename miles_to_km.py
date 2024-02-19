from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

input_box = Entry(width=10)
input_box.grid(row=0,column=1)


my_label = Label(text="Miles", font=("Arial", 22))
my_label.grid(row=0,column=2)
my_label.config(padx=10,pady=10)

my_label2 = Label(text="is equal to", font=("Arial", 22))
my_label2.grid(row=1,column=0)

km_disp = Label(text="0", font=("Arial", 22))
km_disp.grid(row=1,column=1)

my_label = Label(text="Km", font=("Arial", 22))
my_label.grid(row=1,column=2)

# my_label["text"] = "new text"
# my_label.config(text="new text2")
# my_label.config(padx=20,pady=20)


def button_clicked():
    #my_label.config(text="button clicked")
    miles = int(input_box.get())
    kilo_meters = miles * 1.60934
    km_disp.config(text=kilo_meters)


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2,column=1)





# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 3, 5))

window.mainloop()
