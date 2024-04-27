# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import *

import pyperclip

# Until now we were storing data in different formate but it is not good formate, so let's store data in JSON formate
# Then we can use write read and update operations in python

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwordEntry.insert(0, password)
    pyperclip.copy(password) # now i can paste it whenver i want , do methods like copy and pasting stuff



# ---------------------------- SAVE PASSWORD ------------------------------- #

# save data in data.txt file
# Formate the way you like
# It is not class it is another module of code in tkinter so * will not import this
from tkinter import messagebox


def save():
    with open('data.txt', mode="a") as file:
        website = websiteEntry.get()
        email = usernameEntry.get()
        password = passwordEntry.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="OOPS", message="Please make sure to add password and website name")
        else:
            # messagebox.showinfo(title="Title",message="message")
            isOk = messagebox.askokcancel(title=website,
                                          message=f"This are the details entered \nEmail:  {email} \nPassword: {password}")
            if isOk:
                file.write(f"{website} | {email} | {password}\n")
                websiteEntry.delete(0, END)
                # usernameEntry.delete(0,END)
                passwordEntry.delete(0, END)

    # let's say user that you have successfully entered items MessageBoxes


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk(screenName="Password generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
# https://tkdocs.com/tutorial/canvas.html
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

websiteLable = Label(text="Website : ")
websiteLable.grid(row=1, column=0, )
websiteEntry = Entry(width=90)
websiteEntry.grid(column=1, row=1, columnspan=2)
websiteEntry.focus()  # add pointer in start

usernameLable = Label(text="Username : ")
usernameLable.grid(row=3, column=0)
usernameEntry = Entry(width=90)
usernameEntry.grid(column=1, row=3, columnspan=2)
usernameEntry.insert(0, "ketanrtd1@gmail.com")  # 0 is want to insert at start , if at end then at END

passwordLable = Label(text="Password : ")
passwordLable.grid(row=5, column=0)
passwordEntry = Entry(width=70)
passwordEntry.grid(column=1, row=5)

genratePassword = Button(text="Generate Password", command=generate_password)
genratePassword.grid(row=5, column=2)

addButton = Button(text="ADD", width=80, command=save)
addButton.grid(row=7, column=0, columnspan=3)

window.mainloop()
