
# questionNumber and questionList and also one method of next question

class Quizbrain:

    def __init__(self, question_list):  # get the question_list
        self.questionList = question_list
        self.questionNumber = 0 # should in initialise or in outside in class
        self.score = 0

    def still_has_question(self):
        if self.questionNumber < len(self.questionList):
            return True
        return False


    def nextQuestion(self):
        current_question = self.questionList[self.questionNumber]
        self.questionNumber += 1
        user_ans = input(f"Q.{self.questionNumber} {current_question.text} ( True / False ) ? ")
        self.check_answer(user_ans,current_question.answer)

    def check_answer(self,user_ans,correct_ans):
        if(user_ans == correct_ans):
            print("You got it right :))")
            self.score += 1
        else:
            print("That's wrong :| ")
        print(f"The correct answer is {correct_ans}.")
        print(f"Your current score is {self.score}/{self.questionNumber}")

