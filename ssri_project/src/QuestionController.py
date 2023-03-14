from datetime import datetime
from information_processor_model import QuestionModel

class QuestionController: 

    def __init__(self, number_of_questions, medication): 
        self.answers = [None] * number_of_questions
        self.medication = medication

    def extract_information(self, id, question_id): 
        question_id = int(question_id)
        if id == None: 
            pass 
        else: 
            id = abs(id) - 1
            # -1 for indexing 
            self.answers[question_id-1] = id
        print(self.answers)
        return id 
    
    def change_medication(self, medication):
        self.medication = medication
        print(self.medication)
    # dictionary to pass this into the database 
    def construct_dictionary(self): 
        answers_dict = {} 
        # Assume that the words are constructed in question order
        for i in range(len(self.answers)): 
            answers_dict[i+1] = self.answers[i] 
        return answers_dict
    