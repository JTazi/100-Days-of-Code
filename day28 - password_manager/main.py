from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

PASSWORD_FILE = "passwords.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    #select random characters for password
    password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    #join lists of characters and shuffle
    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
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
    full_entry = website_entry.get() +"|"+ username_entry.get() +"|"+ password_entry.get() +"\n"
    #check if entries are blank
    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning(title='URL or Password Error',message="Either the URL or password was left blank, please fix and try again.")
    else:
        #verify user intent
        is_ok = messagebox.askyesno(title=website_entry.get(),message="Are you sure you want to save username/password?")
        if is_ok:
            #open txt and save entry
            with open(PASSWORD_FILE,'a') as f:
                f.write(full_entry)
            #clear entries for next 
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()


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

gen_password_button = Button(text="Generate password", command=password_generator)
gen_password_button.grid(row=4,column=3)

add_button = Button(text="Add",width=36, command=save_entry)
add_button.grid(row=5,column=2,columnspan=2)

#Entries
website_entry = Entry(width=40)
website_entry.grid(row=2,column=2,columnspan=2)
website_entry.focus()

username_entry = Entry(width=40)
#Add some text to begin with
username_entry.insert(END, string="email@email.com")
username_entry.grid(row=3,column=2,columnspan=2)

password_entry = Entry(width=21)
# #Gets text in entry
# print(entry.get())
password_entry.grid(row=4,column=2)

window.mainloop()

