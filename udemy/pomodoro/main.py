from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
TIME = None

# Initialize
screen = Tk()
screen.title("Pomodoro Timer")
screen.config(padx=100, pady=30, bg=YELLOW)
reps = 0

def starter():
    """Starts the timer"""
    global reps
    reps += 1
    if reps % 6 == 0:
        text.config(text="Long Break", font=(FONT_NAME, 20, 'bold'), fg=RED)
        counter(LONG_BREAK_SEC)
    elif reps % 2 == 0:
        text.config(text="Short Break", font=(FONT_NAME, 20, 'bold'), fg=PINK)
        counter(SHORT_BREAK_SEC)
    else:
        text.config(text="Work Time", font=(FONT_NAME, 20, 'bold'), fg=GREEN)
        counter(WORK_SEC)

def resetter():
    """Resets the timer"""
    global TIME, reps
    if TIME is not None:
        screen.after_cancel(TIME)
    text.config(text="Timer", font=(FONT_NAME, 20, 'bold'), fg=PINK)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0

def counter(count):
    """Counts down and updates the timer display."""
    mins = f"{count // 60:02}"
    secs = f"{count % 60:02}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global TIME
        TIME = screen.after(1000, counter, count - 1)
    else:
        # Update check marks after a work session
        if reps % 2 == 0:
            checkmarks = "✔" * (reps // 2)
            check_mark.config(text=checkmarks)
        starter()

# UI Components
text = Label(text="Timer", font=(FONT_NAME, 20), bg=YELLOW, fg=PINK)
text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
try:
    img = PhotoImage(file="tomato.png")
    canvas.create_image(102, 112, image=img)
except:
    print("Image file 'tomato.png' not found.")
timer_text = canvas.create_text(100, 118, text="00:00", fill="black", font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=starter, highlightthickness=0, font=(FONT_NAME, 10, 'bold'), bg=GREEN, fg=YELLOW)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=resetter, highlightthickness=0, font=(FONT_NAME, 10, 'bold'), bg=RED, fg=YELLOW)
reset.grid(row=2, column=2)

check_mark = Label(font=(FONT_NAME, 12, 'bold'), fg=PINK, bg=YELLOW)
check_mark.grid(row=2, column=1)

# Main loop
screen.mainloop()
