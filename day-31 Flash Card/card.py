import random
from tkinter import *

FRENCH_CARD = "#609966"
ENGLISH_CARD = "#004D25"
TEXT = "#02231c"
FONT_LG = ('Arial', 16, 'bold')
FONT_WORD = ('Arial', 24, 'bold')

class CardManager(Canvas):

    def __init__(self, data):
        super().__init__(width=400, height=300, bg=FRENCH_CARD)
        self.data = data
        self.grid(row=0, column=1)

        self.timer = self.create_text(370, 30, text="3", fill='white', anchor='center', font=FONT_WORD)
        self.language = self.create_text(200, 50, text="", fill='white', anchor='center', font=FONT_LG)
        self.word = self.create_text(200, 150, text="", fill='white', anchor='center', font=FONT_WORD)
    
    def create_card(self):
        self.curr_word = random.choice(self.data)
        self.itemconfig(self.language, text="French")
        self.itemconfig(self.word, text=self.curr_word["french"])

    def swap_language(self):
        self.itemconfig(self.language, text="English")
        self.itemconfig(self.word, text=self.curr_word["english"])
    
    def modify_timer(self, secs):
        self.itemconfig(self.timer, text=secs)
    
    def remove_card(self):
        self.data.remove(self.curr_word)
