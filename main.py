import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Label", font=("Arial", 22))
my_label.pack()


# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 3, 5))

window.mainloop()
