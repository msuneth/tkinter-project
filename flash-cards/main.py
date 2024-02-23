from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import math
import json
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
FIRST_LANGUAGE = "French"
current_word = (None, None)


def get_random_word() -> tuple:
    df = None
    try:
        df = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        df = pandas.read_csv("data/french_words.csv")
    finally:
        random_word_row = df.sample()
        random_french_word = random_word_row["French"].squeeze()
        random_english_word = random_word_row["English"].squeeze()
        global current_word
        current_word = random_french_word, random_english_word
        return current_word


def right_button_clicked():
    global current_word
    # remove current word from list n save new csv words_to_learn.csv
    df = None
    try:
        df = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        df = pandas.read_csv("data/french_words.csv")
    finally:
        df = df[df['French'] != current_word[0]]
        df.to_csv("data/words_to_learn.csv", index=False)
        display_random_word()


def wrong_button_clicked():
    display_random_word()


def display_random_word():
    global flip_timer
    window.after_cancel(flip_timer)
    random_word = get_random_word()
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{random_word[0]}", fill="black")
    # word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
    flip_timer = window.after(3000, display_english_word, random_word)


def display_english_word(random_word: tuple):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{random_word[1]}", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(background=BACKGROUND_COLOR)
language_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_button_clicked)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_button_clicked)
wrong_button.grid(row=1, column=0)


flip_timer = window.after(100, display_random_word)

window.mainloop()
