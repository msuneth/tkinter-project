import time
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import math
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_clicked():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    # for char in password_list:
    #     password += char

    print(f"Your password is: {password}")
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_clicked():
    website_name = website_entry.get()
    password = ""
    email_username = ""

    if len(website_name) == 0:
        messagebox.showwarning("Website Empty", message="Please fill the website name!")
    else:
        # is_ok = messagebox.askokcancel(title=website_name, message=f"Please confirm to save below information\n"
        #                                                            f"Email/Username: {email_username}\n"
        #                                                            f"Password: {password}")
        # if is_ok:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
            email_username = data[website_name]["email_username"]
            password = data[website_name]["password"]
        except FileNotFoundError:
            messagebox.showwarning(title="File not found", message="No Data File found")
            # with open("data.json", "w") as file:
            #     json.dump(new_data, file, indent=4)
        except KeyError:
            messagebox.showwarning(title="Data not found", message="No details for the website exists")
        else:
            messagebox.showinfo(title=website_name, message=f"Email/Username: {email_username}\n"
                                                            f"Password: {password}")
            # with open("data.txt", "a") as file:
            #     file.writelines(f"{website_name} | {email_username} | {password}\n")
            # status_label.config(text="Password data saved")
            # status_label.config(text="")
            # website_entry.delete(0, 'end')
            # password_entry.delete(0, 'end')
            # status_label.config(text="")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password_clicked():
    website_name = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website_name: {
            "email_username": email_username,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning("Empty Fields", message="Please fill all fields!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"Please confirm to save below information\n"
                                                                   f"Email/Username: {email_username}\n"
                                                                   f"Password: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                # with open("data.txt", "a") as file:
                #     file.writelines(f"{website_name} | {email_username} | {password}\n")
                status_label.config(text="Password data saved")
                status_label.config(text="")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                status_label.config(text="")


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

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = Button(text="Search",width=14, command=search_clicked)
search_button.grid(row=1, column=2)

email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "msunethbit@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password_clicked)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=add_password_clicked)
add_button.grid(row=4, column=1, columnspan=2)

status_label = Label(text="")
status_label.grid(row=5, column=1)

window.mainloop()
