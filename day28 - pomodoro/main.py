#https://colorhunt.co/
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#counter for which rep of timer the app is on
#pomodoro 25/5/25/5/25/5/25/20 work/rest
iteration = 0

#global var for window obj
window_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_funct():
    global iteration
    global window_timer_sec
    global window_timer_min
    
    window.after_cancel(window_timer_sec)
    window.after_cancel(window_timer_min)
    iteration = 0
    timer.config(text="Timer",fg=GREEN)
    pomo_counter.config(text="")
    canvas.itemconfig(timer_text,text="0:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global iteration
    
    if iteration % 2 == 0:   
        timer.config(text='WORK',fg=GREEN)
        countdown(WORK_MIN)
        iteration +=1
        counter_txt = "X"*(iteration//2+1)
        pomo_counter.config(text=counter_txt)
    elif iteration == 7:
        timer.config(text='BREAK',fg=RED)
        countdown(LONG_BREAK_MIN)
        iteration = 0
    else:
        timer.config(text='BREAK',fg=PINK)
        countdown(SHORT_BREAK_MIN)
        iteration +=1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(minutes,seconds=0):
    global window_timer_sec
    global window_timer_min
    
    if len(str(seconds)) == 1:
        disp_seconds = "0"+str(seconds)
    else:
        disp_seconds = seconds
    canvas.itemconfig(timer_text,text=f"{minutes}:{disp_seconds}")
    if seconds > 0:
        window_timer_sec = window.after(1000,countdown,minutes,seconds-1)
    elif minutes >0:
        window_timer_min = window.after(1000,countdown,minutes-1,59)
    else:    
        start_timer()

    
# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


#create canvas to hold img and timer text
canvas = Canvas(width = 200,height = 224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=2,column=2)

#Labels
timer = Label(text="Timer",font=(FONT_NAME,40,'bold'),bg=YELLOW, fg=GREEN)
timer.grid(row=1,column=2)

pomo_counter = Label(font=(FONT_NAME,14,'bold'),bg=YELLOW, fg=GREEN)
pomo_counter.grid(row=3,column=2)

#Buttons
#calls action() when pressed
start = Button(text="Start", command=start_timer)
start.grid(row=3,column=1)

reset = Button(text="Reset", command=reset_funct)
reset.grid(row=3,column=3)


window.mainloop()