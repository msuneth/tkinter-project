from tkinter import *
import math


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_clicked():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password_clicked():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password_clicked)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=add_password_clicked)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
