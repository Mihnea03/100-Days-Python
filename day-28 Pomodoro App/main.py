# Pomodoro App
# Munteanu Mihnea @ Mihnea03

from tkinter import *
from math import floor

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

def main():
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 32, 'bold'), bg=YELLOW, padx=20, pady=20)
    title_label.grid(column=1, row=0)

    check_marks = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32), pady=10)
    check_marks.grid(column=1, row=3)

    def reset_timer():
        title_label.config(text="Timer", fg=GREEN)
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        check_marks.config(text='')
        global reps
        reps = 0


    def countdown(count):
        if count < 0:
            start_timer()
            global reps
            if reps % 2 == 0:
                check_marks.config(text=int(reps/2) * "✔️")
            return
        
        count_min = floor(count / 60)
        count_sec = count % 60

        if count_min < 10:
            count_min = "0" + str(count_min)
        if count_sec < 10:
            count_sec = "0" + str(count_sec)

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, countdown, count - 1)

    def start_timer():
        global reps
        reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            countdown(long_break_sec)
        elif reps % 2 == 0:
            title_label.config(text="Break", fg=PINK)
            countdown(short_break_sec)
        else:
            title_label.config(text="Work", fg=GREEN)
            countdown(work_sec)
        return

    tomato_photo = PhotoImage(file="tomato.png")
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    canvas.create_image(100, 112, image=tomato_photo)
    timer_text = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 32, 'bold'), fill="white")
    canvas.grid(column=1, row=1)

    start_button = Button(text="Start", highlightthickness=0, bg='white', command=start_timer)
    start_button.grid(column=0, row=2)

    reset_button = Button(text="Reset", highlightthickness=0, bg='white', command=reset_timer)
    reset_button.grid(column=2, row=2)

    window.mainloop()
    return

if __name__ == '__main__':
    main()
