class QuizBrain:
    # Initial attrabutes of the class
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Checking if there are free questions in the array
    def still_has_questions(self):
        if self.question_number > len(self.question_list) - 1:
            print(f"The quiz is over. Your final score: {self.score} / {self.question_number}")
            return False
        else:
            return True

    # Displaying a question and handling user's input
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # Checking user's answer and displaying results
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score} / {self.question_number}\n")