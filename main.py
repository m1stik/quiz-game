from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

# Taking questions from data-file and putting them into array
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

# Shuffling questions in the array and initializing the brain of the quiz
random.shuffle(question_bank)
quiz = QuizBrain(question_bank)

# Displaying questions and results
while quiz.still_has_questions():
    quiz.next_question()