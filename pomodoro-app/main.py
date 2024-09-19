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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start_btn.config(state="normal")
    window.after_cancel(timer)
    timer_lbl.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick_lbl.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start_btn.config(state="disabled")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_lbl.config(text="Break", fg=RED)
        print(long_break_sec / 60)
        print(reps)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_lbl.config(text="Break", fg=PINK)
        print(short_break_sec / 60)
        print(reps)
    else:
        count_down(work_sec)
        timer_lbl.config(text="Work", fg=GREEN)
        print(work_sec / 60)
        print(reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_sec:02}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        start_timer()
        ticks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            ticks += "✔"
        tick_lbl.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_lbl = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
timer_lbl.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", font=("Arial", 12), highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", font=("Arial", 12), highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

tick_lbl = Label(fg=GREEN, bg=YELLOW, font=("Arial", 15))
tick_lbl.grid(column=1, row=3)

window.mainloop()
