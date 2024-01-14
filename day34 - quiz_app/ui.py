from tkinter import  *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

def action():
    pass

class QuizInterface():
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question_text = self.canvas.create_text(150,125,text="questions go here",font=("Arial",20,'italic'),width=280)
        self.canvas.grid(row=2,column=1,columnspan=2)
        
        self.true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image = self.true_image, highlightthickness=0,command=self.check_answ_true)
        self.true_button.grid(row=3,column=1,padx=20,pady=20)
        
        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image = self.false_image, highlightthickness=0, command=self.check_answ_false)
        self.false_button.grid(row=3,column=2,padx=20,pady=20)
        
        self.score_label = Label(text =  "Score: 0")
        self.score_label.config(bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=1,column=2,padx=20,pady=20)

        #future work  to add dropdown of categories to give player option of trivia categories
        # self.OPTIONS = [
        #     "egg",
        #     "bunny",
        #     "chicken"
        # ]
        
        
        # self.variable = StringVar(self.window)
        # self.variable.set(self.OPTIONS[0]) # default value
        
        # self.w = OptionMenu(self.window, self.variable, *self.OPTIONS)
        # self.w.grid(row=1,column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"Game Over\nFinal score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def check_answ_true(self):
        self.feedback(self.quiz.check_answer('true'))
        
    def check_answ_false(self):
        self.feedback(self.quiz.check_answer('false'))
            
    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000,self.get_next_question)
            

        
        
    
        