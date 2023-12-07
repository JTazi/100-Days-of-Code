from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#create list of question objects from question_data
q_bank = []
for qd in question_data['results']:
    q = Question(qd['question'],qd['correct_answer'])
    q_bank.append(q)
    
quiz = QuizBrain(q_bank)

while quiz.still_has_questions():

    quiz.next_question()
    
print(f"Game Over! Final Score: {quiz.score}/{quiz.question_number}")