from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range (0, len(question_data)):
    question_loop = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(question_loop)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"Congratulations You have completed the Quiz\nYour Final Score is {quiz.score}/{quiz.question_number}")
