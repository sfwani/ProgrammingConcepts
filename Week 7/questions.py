'''
This code defines a class called "Question" that represents a single trivia question with its four possible answer options and the correct answer.
The constructor method initializes the class variables with the question and its answer options.
The __str__() method returns a formatted string that displays the question and its answer options in a readable format.
'''

class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def __str__(self):
        return f"{self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}"
