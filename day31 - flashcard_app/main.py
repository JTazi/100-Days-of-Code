#dependencies
from tkinter import *
import pandas as pd
from random import randint

#Constants

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'

#---------create_flashcards--
#read data from french_words.csv
try:
    df = pd.read_csv('data/words_to_learn.csv')
except:
    df = pd.read_csv('data/french_words.csv')
#get list of dict{french:english},
lang_dict = df.to_dict(orient = 'records')

index=0

def red_button():
    global index,after_id
    
    window.after_cancel(after_id)
    
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text,text='French')
    index = randint(1,len(lang_dict)-1)
    french = lang_dict[index]['French']
    canvas.itemconfig(word_text,text=french)
    
    after_id = window.after(3000,flip)
    
def green_button():
    global index,after_id
    window.after_cancel(after_id)
    if index != 0:
        lang_dict.pop(index)
    
    df_to_learn = pd.DataFrame(lang_dict)
    df_to_learn.to_csv('data/words_to_learn.csv',index=False)
    
    red_button()

def flip():
    global index
    canvas.itemconfig(canvas_image, image=back_image)
    english = lang_dict[index]['English']
    canvas.itemconfig(title_text,text='English')
    canvas.itemconfig(word_text,text=english)

#----------UI/UX-------------

#Creating a new window and configurations
window = Tk()
window.title("Flash Cards")

window.config(bg=BACKGROUND_COLOR)
after_id = window.after(3000,green_button)
#Buttons

#calls action() when pressed
x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=red_button)
x_button.grid(row=2,column=1,pady=50)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=green_button)
check_button.grid(row=2,column=2,pady=50)

#Canvas for text
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width = 800,height = 526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(400,263, image=front_image)

title_text = canvas.create_text(400,150,text="Title",fill='black',font=(FONT_NAME,40,'bold'))
word_text = canvas.create_text(400,263,text="Word",fill='black',font=(FONT_NAME,60,'bold'))
canvas.grid(row=1,column=1,columnspan = 2,padx=50,pady=50)

window.mainloop()
