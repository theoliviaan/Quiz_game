from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# print(question_data[0]["text"])

question_bank = []

# create question bank of question objects
for text in question_data:
    question = text["question"]
    answer = text["correct_answer"]
    new_q = Question(question, answer)
    question_bank.append(new_q)

# print(question_bank[0].text)

quiz = QuizBrain(question_bank) # the value "question_bank" replaces the q_list from the QuizBrain class

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz!\nYour final score is {quiz.score}/{quiz.question_number}")






