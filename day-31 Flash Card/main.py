# Flash Card
# Munteanu Mihnea @ Mihnea03

from tkinter import *
from tkinter import messagebox
from data import get_data, write_missed_words
from card import CardManager

BG = "#EDF1D6"
BTN_FONT = ('Arial', 30)
SECONDS = 3

timer = None

def main():
    missed_words = []

    data = get_data()
    window = Tk()
    window.config(padx=50, pady=30, bg=BG)
    window.minsize(width=500, height=400)
    window.title("Flash Cards")
    card_manager = CardManager(data)

    def start_countdown(secs):
        if secs < 0:
            card_manager.swap_language()
            return
        card_manager.modify_timer(secs)
        global timer
        timer = window.after(1000, start_countdown, secs - 1)

    def any_button():
        window.after_cancel(timer)
        try:
            card_manager.create_card()
        except IndexError:
            messagebox.showwarning(title="Good Job!", message="You know all the words! Exiting program...")
            quit()
        else:
            start_countdown(SECONDS)

    def correct():
        card_manager.remove_card()
        any_button()
        pass

    def wrong():
        missed_words.append(card_manager.curr_word)
        any_button()
        pass

    # Buttons
    yes_btn = Button(text="✔️", font=BTN_FONT, bg=BG, fg='green', highlightthickness=0, command=correct)
    yes_btn.grid(row=1, column=2)

    no_btn = Button(text="✖️", font=BTN_FONT, bg=BG, fg='red', highlightthickness=0, command=wrong)
    no_btn.grid(row=1, column=0)

    card_manager.create_card()
    start_countdown(SECONDS)

    window.mainloop()
    write_missed_words(missed_words)
    return

if __name__ == '__main__':
    main()
