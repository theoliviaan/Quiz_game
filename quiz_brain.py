

class QuizBrain:

    def __init__(self, q_list):
        # Because all our question will start from 0 and will keep track of the questions our users are currently on
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    # retrieve the item at the current question number from the question list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # which also means question_bank[0] since it starts from 0
        self.question_number += 1 # to increase the number to start from 1
        user_input = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        # Basically , Q.1 : question_bank[0]["text"] (True/False):
        self.check_answer(user_input, current_question.correct_answer)

    def check_answer(self, u_input, correct_answer):
        if u_input.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was : {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}\n")




