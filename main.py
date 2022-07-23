from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import xlwt
from xlwt import Workbook


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_input.delete(0, END)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    text = f'{website} | {username} | {password} \n'

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='Please do not leave blank fields')
    else:
        is_okay = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {username}\nPassword: {password}\nIs this okay to submit?')
        if is_okay:
            # wb = Workbook()
            # passwords = wb.add_sheet('Passwords')
            with open('password-file.txt', 'a') as file:
                file.write(text)
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='black')

# Canvas
bg_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, bg='black', highlightthickness=0)
canvas.create_image(100, 94.5, image=bg_image)
canvas.grid(column=2, row=1)

# Website Label
website_label = Label(text='Website:', fg='white', bg='black')
website_label.grid(column=1, row=2)

# Username Label
username_label = Label(text='Email/Username:', fg='white', bg='black')
username_label.grid(column=1, row=3)

# Password Label
password_label = Label(text='Password:', fg='white', bg='black')
password_label.grid(column=1, row=4)

# Website input
website_input = Entry(fg='white', bg='black', width=35)
website_input.grid(column=2, row=2, pady=1, columnspan=2)

# Username Input
username_input = Entry(fg='white', bg='black', width=35)
username_input.grid(column=2, row=3, pady=1, columnspan=2)
username_input.insert(0, 'raleighdex@gmail.com')

# Password Input
password_input = Entry(fg='white', bg='black', width=21)
password_input.grid(column=2, row=4, pady=1)

# Password Generate Button
password_gen_button = Button(text='Generate Password', fg='black', highlightbackground='black', bg='white', command=generate_password)
password_gen_button.grid(column=3, row=4)

# Add button
add_button = Button(text='Add', fg='black', borderwidth=0, highlightbackground='black', width=36, command=save_password)
add_button.grid(column=2, columnspan=2, row=5)


window.mainloop()