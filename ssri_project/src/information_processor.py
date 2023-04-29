from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import sqlite3 
from sqlite3 import Error
import datetime as dt
from .digitaltwin import DigitalTwin

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

# Represents the table of data 
class QuestionModel(QtCore.QAbstractListModel):
    def __init__(self, *args, question=None, **kwargs):
        super(QuestionModel, self).__init__(*args, **kwargs)
        self.connection = self.create_connection()
        self.question = question 
        self.column_list = ["question1", "question2", "question3", "question4", "question5","question6,","question7",
        "question8", "question9", "question10", "question11", "question12", "question13", "question14"]

    def data(self):
        return self.question

    def create_connection(self): 
        con = None
        try:
            con = sqlite3.connect("db/antidepressant.db")
        except Error as e:
            print(e)
        else:
            con.row_factory = dict_factory
            return con

    def create_answer(self, medication, answer_list, user):
        with self.connection as con:
            today = dt.date.today().strftime('%Y-%m-%d')
            cur = con.cursor()
            cur.execute("INSERT INTO wellbeing(user_id, date, antidepressant, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user, today, medication, answer_list[0], answer_list[1], answer_list[2], answer_list[3], answer_list[4], answer_list[5], answer_list[6], answer_list[7], answer_list[8], answer_list[9], answer_list[10], answer_list[11], answer_list[12], answer_list[13]))
            con.commit()
        return cur.lastrowid

    def get_id_value(self, id): 
        with self.connection as con:
            res = con.execute("SELECT * FROM wellbeing WHERE user_id = ?", (id,))
            res = res.fetchall()
        return res 

    def get_all_values(self, user):
        with self.connection as con:
            res = con.execute("SELECT * FROM wellbeing WHERE user_id = ?", (user,))
            res = res.fetchall()
            con.close()
        return res 

    # Refactor this later 
    def construct_data_dictionary(self, antidepressant_list, score_list, date_list):    
        score_dictionary = dict()
        for i in range(len(antidepressant_list)):
            antidepressant = antidepressant_list[i]
            score = score_list[i]
            date = date_list[i]
            if antidepressant not in score_dictionary:
                score_dictionary[antidepressant] = []
            score_dictionary[antidepressant].append((date, score))
        print(score_dictionary)
        return score_dictionary
    
    def digital_twin_training(self, question_answers=None, medication=None, user_id=None):
        # Get values and insert items into the database 
        if question_answers is not None and medication is not None: 
            self.create_answer(medication, question_answers, user_id)
        
        training_data = self.get_id_value(user_id)

        digital_twin = DigitalTwin(self.column_list)
        total_scores = digital_twin.total_scores(training_data)

        score_dictionary = self.construct_data_dictionary(total_scores[0], total_scores[1], total_scores[2])    
        digital_twin.fit_regression_model(score_dictionary)
