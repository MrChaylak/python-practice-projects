from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CLEAR ENTRIES ------------------------------- #
def clear_entries():
    website_entry.delete(0, END)
    # email_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().lower()
    if len(website) == 0:
        return None
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showinfo(title="Error", message="No data found.")
        else:
            if website in data:
                pyperclip.copy(data[website]["password"])
                messagebox.showinfo(title=website.capitalize(), message=f"Email: {data[website]["email"]}\n"
                                                           f"Password: {data[website]["password"]}")
            else:
                messagebox.showinfo(title="No Website Details", message="No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # data = f"{website} | {email} | {password}\n"
    # print(data)
    if len(website) == 0 or len(password) == 0:
        print("Empty fields!")
        messagebox.showinfo(title="Empty Fields", message="Website name or password can't be empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                if website in data:
                    update = messagebox.askyesno("Warning", f"There is already a password saved for "
                                                            f"{website.capitalize()}.\nWould you like to overwrite?")
                    if update:
                        pass
                    else:
                        return None
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        finally:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email:")
email_lbl.grid(column=0, row=2)

password_lbl = Label(text="Pasword:")
password_lbl.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky=EW)
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_entry.insert(0, "example@email.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=EW)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky=EW)

add_btn = Button(text="Add", command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky=EW)

search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky=EW)

clear_btn = Button(text="Clear", command=clear_entries)
clear_btn.grid(column=0, row=4, sticky=EW)

window.mainloop()
