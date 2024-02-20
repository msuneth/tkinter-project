from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def start_button_clicked():
    global rounds
    rounds += 1
    if rounds % 8 == 0:
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(LONG_BREAK_MIN * 60)
    elif rounds % 2 == 0:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(WORK_MIN * 60)
    #count_down(SHORT_BREAK_MIN * 60)
    # count_down(WORK_MIN * 60)
    # count_down(SHORT_BREAK_MIN * 60)
    # count_down(WORK_MIN * 60)
    # count_down(SHORT_BREAK_MIN * 60)
    # count_down(WORK_MIN * 60)
    # count_down(LONG_BREAK_MIN * 60)
    # timer_round = 1
    # while True:
    #     count_down(WORK_MIN * 60)
    #     if timer_round % 4 != 0:
    #         count_down(SHORT_BREAK_MIN * 60)
    #     else:
    #         count_down(LONG_BREAK_MIN * 60)
    #     timer_round += 1


def reset_button_clicked():
    window.after_cancel(timer)
    checkmark_label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    global rounds
    rounds = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_down_min = math.floor(count / 60)
    print(count_down_min)
    if count_down_min < 10:
        count_down_min = f'0{count_down_min}'
    count_down_sec = count % 60
    if count_down_sec < 10:
        count_down_sec = f'0{count_down_sec}'
    canvas.itemconfig(timer_text, text=f"{count_down_min}:{count_down_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        if rounds % 2 == 0:
            number_of_checks = int(rounds / 2)
            check_mark = ""
            for _ in range(number_of_checks):
                check_mark += "✔"
            checkmark_label.config(text=check_mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
        start_button_clicked()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_button_clicked)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_button_clicked)
reset_button.grid(row=2, column=3)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(row=3, column=1)

window.mainloop()
