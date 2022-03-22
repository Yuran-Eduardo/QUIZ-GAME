

class QuizBrain:
  def __init__(self,question_list):
    self.question_list = question_list
    self.question_number = 0
    self.score = 0

  def still_has_question(self):
    return self.question_number < len(self.question_list)
    
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answers(user_answer, current_question.answer,self.score,self.question_number)

  def check_answers(self, user_answer, correct_answer,score,question_number):
    if user_answer.lower() == correct_answer.lower():
      score += 1
      print("You got it right")
    else:
      print("Thats Wrong")
    print(f"The correct answer was: {correct_answer}")
    print(f"Your Score is {score}/{question_number}")
    print("\n")