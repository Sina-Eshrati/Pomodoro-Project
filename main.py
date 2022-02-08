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
cycle = 1
reset = False


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global cycle
    global reset
    reset = True
    cycle = 1
    checkmark["text"] = ""
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reset
    reset = False
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if cycle < 9:
        if cycle % 2 != 0:
            count_down(work_sec)
            label.config(text="Work", fg=GREEN)
        elif cycle % 2 == 0 and cycle != 8:
            count_down(short_break_sec)
            label.config(text="Break", fg=PINK)
            checkmark["text"] = checkmark["text"] + "✔"
        else:
            count_down(long_break_sec)
            label.config(text="Break", fg=RED)
            checkmark["text"] = checkmark["text"] + "✔"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global cycle
    if not reset:
        minute = math.floor(count / 60)
        second = count % 60
        if second < 10:
            second = f"0{second}"
        if minute < 10:
            minute = f"0{minute}"
        canvas.itemconfig(canvas_text, text=f"{minute}:{second}")
        if count > 0:
            window.after(1000, count_down, count-1)
        else:
            cycle += 1
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"), pady=20)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

btn_start = Button(text="Start", bd=0, bg="#f05945", fg=YELLOW, font=("Arial", 10, "bold"), command=start_timer)
btn_start.grid(column=0, row=2)
btn_reset = Button(text="Reset", bd=0, bg="#f05945", fg=YELLOW, font=("Arial", 10, "bold"), command=reset_timer)
btn_reset.grid(column=2, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN, font=("Arial", 15, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
