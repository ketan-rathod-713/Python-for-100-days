from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i["text"],i["answer"]))

quiz = Quizbrain(question_bank)

while quiz.still_has_question():
    quiz.nextQuestion()

print("Finally completed Quiz ")
print(f"Your final score is {quiz.score}/{quiz.questionNumber}")
print("\n")

# So OOPs is very structured we can change any object by keeping it's functionalities same