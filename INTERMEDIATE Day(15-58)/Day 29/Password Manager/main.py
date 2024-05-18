from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(5, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 2))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 3))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Not details for {website} exists.")











# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Bg Image
canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(55, 100, image=password_logo)
canvas.grid(column=1, row=0, columnspan=3)


# Websites
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=15)
website_input.grid(row=1, column=1)
website_input.focus()


# Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=33)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "sumit@gmail.com")


# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=15)
password_input.grid(row=3, column=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)


# Search
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)


# Add
add_button = Button(text="Add", width=28, command=save)
add_button.grid(row=4, column=1, columnspan=2)










window.mainloop()