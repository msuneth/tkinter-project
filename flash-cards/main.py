from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import math
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(background=BACKGROUND_COLOR)
language_text = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1,column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1,column=1)

#
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_username_label = Label(text="Email/Username:")
# email_username_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)
#
# website_entry = Entry(width=32)
# website_entry.grid(row=1, column=1)
# website_entry.focus()
# search_button = Button(text="Search",width=14, command=search_clicked)
# search_button.grid(row=1, column=2)
#
# email_username_entry = Entry(width=50)
# email_username_entry.grid(row=2, column=1, columnspan=2)
# email_username_entry.insert(0, "msunethbit@gmail.com")
# password_entry = Entry(width=32)
# password_entry.grid(row=3, column=1)
#
# generate_password_button = Button(text="Generate Password", command=generate_password_clicked)
# generate_password_button.grid(row=3, column=2)
#
# add_button = Button(text="Add", width=43, command=add_password_clicked)
# add_button.grid(row=4, column=1, columnspan=2)
#
# status_label = Label(text="")
# status_label.grid(row=5, column=1)

window.mainloop()


