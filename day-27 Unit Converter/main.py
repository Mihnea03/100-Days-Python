# Unit Converter
# Munteanu Mihnea @ Mihnea03

from tkinter import *

KM_FACTOR = 1.609344

def main():
    window = Tk()
    window.title("Unit Converter")
    window.minsize(width=400, height=100)
    window.config(padx=20, pady=20)

    miles = Label(text='Miles', font=('Arial', 16), anchor='center')
    is_equal = Label(text='is equal to', font=('Arial', 16))
    km = Label(text='Km', font=('Arial', 16), anchor='center')
    km_calculated = Label(text='0', font=('Arial', 16))

    def calculate_km():
        km_eq = int(miles_input.get()) * KM_FACTOR
        km_calculated.config(text=round(km_eq))

    miles_input = Entry(font=('Arial', 16))
    calculate = Button(text='Calculate', command=calculate_km, font=('Arial', 16))

    miles_input.grid(row=0, column=1)
    miles.grid(row=0, column=2)
    is_equal.grid(row=1, column=0)
    km_calculated.grid(row=1, column=1)
    km.grid(row=1, column=2)
    calculate.grid(row=2, column=1)

    window.mainloop()
    return

if __name__ == '__main__':
    main()
