# Password Manager
# Munteanu Mihnea @ Mihnea03

from tkinter import *
from tkinter import messagebox
import string
import random
import json

LOGO = 'logo.png'
DATA = 'data.json'
LENGTH = 10
ASK_FORMAT = """Email: {}
Password: {}
Is this ok?
"""

def write_to_file(website, username, password):
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    try:
        with open(DATA, 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open(DATA, 'w') as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open(DATA, 'w') as data_file:
            json.dump(data, data_file, indent=4)
    return

def random_password():
    pick = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pass_list = random.choices(population=pick, k=LENGTH)
    password = "".join(pass_list)
    return password

def main():
    window = Tk()
    window.title('My Pass')
    window.config(bg='white', padx=40, pady=40)
    window.minsize(400, 400)

    logo = Canvas(width=200, height=200, bg='white', highlightthickness=0)
    logo_img = PhotoImage(file=LOGO)
    logo.create_image(100, 100, image=logo_img)
    logo.grid(row=0, column=1)

    wb = Label(text="Website:", bg='white')
    em_un = Label(text="Email/Username:", bg='white')
    pas = Label(text="Password:", bg='white')

    wb.grid(row=1, column=0)
    em_un.grid(row=2, column=0)
    pas.grid(row=3, column=0)

    website = StringVar()
    wb_input = Entry(textvariable=website)

    email_user = StringVar()
    em_un_input = Entry(textvariable=email_user, width=36)

    password = StringVar()
    pas_input = Entry(textvariable=password, width=21)

    wb_input.grid(row=1, column=1)
    em_un_input.grid(row=2, column=1, columnspan=2)
    pas_input.grid(row=3, column=1)

    def generate_password():
        random_pass = random_password()
        window.clipboard_clear()
        window.clipboard_append(random_pass)
        password.set(random_pass)
        return

    generate_pass = Button(text="Generate Password", command=generate_password, bg='white')
    generate_pass.grid(row=3, column=2)

    def clear_inputs():
        password.set("")
        email_user.set("")
        website.set("")

    def add_password():
        web = website.get()
        user = email_user.get()
        passw = password.get()

        if web == '' or user == '' or passw == '':
            messagebox.showwarning('Invalid input!', 'Input is invalid! It should not contain empty fields!')
        else:
            if messagebox.askyesno(title=f'{web}', message=ASK_FORMAT.format(user, passw)) is True:
                write_to_file(website=web, username=user, password=passw)
                clear_inputs()
        return
    
    add_button = Button(text="Add", command=add_password, width=33, bg='white')
    add_button.grid(row=4, column=1, columnspan=2)

    def search_website():
        try:
            with open(DATA, 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        
        name = website.get()

        try:
            web = data[name]
        except KeyError:
            messagebox.showwarning(title="Error", message="No website with that name is saved!")
        else:
            messagebox.showinfo(title=website.get(), message=f"Email: {web['email']}\nPassword: {web['password']}")
        return

    search = Button(text="Search", command=search_website, bg='white')
    search.grid(row=1, column=2)

    window.mainloop()
    return


if __name__ == '__main__':
    main()
