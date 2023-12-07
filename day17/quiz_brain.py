class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        #retrieve the item at the current question_number from the question_list
        #use input to show question and get answer
        question = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number +=1
        user_answer = input(f'Q.{self.question_number} {question} (True/False)?:')
        self.check_answer(answer, user_answer)
        print(f'Current score: {self.score}/{self.question_number}')
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,correct_ans, user_ans):
        if correct_ans.lower() == user_ans.lower():
            self.score +=1
            print("That's Correct!")
        else:
            print(f"That's Wrong, Right Answer is {correct_ans}.")
            