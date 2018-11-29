from mongoengine import *

class Questions(Document):
    results = ListField()
    category = StringField()
    types =  StringField()
    difficulty = StringField()
    question = StringField()
    correct_answer = StringField()
    incorrect_answers = ListField()

    # def __str__(self):
    #     return "{0} {1} {2} {3}".format(self.category, self.question, self. correct_answer, self.incorrect_answers)