from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

PASSWORD_FILE = "passwords.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    #select random characters for password
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    #join lists of characters and shuffle
    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)
    #convert list into string
    password = "".join(password_list)
    #clear password entry box and populate with newly generated password
    password_entry.delete(0,END)
    password_entry.insert(END,string=password)
    #copy password to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():

    #collect data from entries
    data_dict = {
        website_entry.get():{
            'username':username_entry.get(),
            'password':password_entry.get()
            }
        }
    #check if entries are blank
    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title='URL or Password Error',message="Either the URL or password was left blank, please fix and try again.")
    else:
        #verify user intent
        is_ok = messagebox.askyesno(title=website_entry.get(),message="Are you sure you want to save username/password?")
        if is_ok:
            #open txt and save entry
            with open(PASSWORD_FILE,'r') as f:
                try:
                    #if it's the first time and the password file is empty, will error
                    data = json.load(f)
                    data.update(data_dict)
                except:
                    data = data_dict
            with open(PASSWORD_FILE,'w') as f:
                json.dump(data,f,indent=4)
            #clear entries for next 
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

#-----------------------------SEARCH----------------------------------- #
def search():
    website = website_entry.get()
    
    with open(PASSWORD_FILE,'r') as f:
        data = json.load(f)
    try:
        search_username = data[website]['username']
        search_password = data[website]['password']
        messagebox.showinfo(title = website,message=f"Username: {search_username}\nPassword: {search_password}")
    except:
        messagebox.showerror(title = "Search Error",message = "No Listing for that Website exists")
    website_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width = 200,height = 200,highlightthickness=0)
pass_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=pass_img)
canvas.grid(row=1,column=2)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=2,column=1)

username_label = Label(text="Email/Username:")
username_label.grid(row=3,column=1)

password_label = Label(text="Password:")
password_label.grid(row=4,column=1)

#Buttons

gen_password_button = Button(text="Generate", command=password_generator)
gen_password_button.grid(row=4,column=3)

add_button = Button(text="Add",width=36, command=save_entry)
add_button.grid(row=5,column=2,columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=2,column=3)

#Entries
website_entry = Entry(width=25)
website_entry.grid(row=2,column=2,columnspan=2)
website_entry.focus()

username_entry = Entry(width=25)
#Add some text to begin with
username_entry.insert(END, string="email@email.com")
username_entry.grid(row=3,column=2,columnspan=2)

password_entry = Entry(width=21)
# #Gets text in entry
# print(entry.get())
password_entry.grid(row=4,column=2)

window.mainloop()

