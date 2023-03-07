from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import sqlite3 
from sqlite3 import Error
from digitaltwin import DigitalTwin

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

    def rowCount(self, index):
        return len(self.question)

    def create_connection(self): 
        con = None
        try:
            con = sqlite3.connect("db/antidepressant.db")
        except Error as e:
            print(e)
        else:
            con.row_factory = dict_factory
            return con

    def create_answer(self, con, answer):
        sql = '''INSERT INTO wellbeing(date, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cur = con.cursor()
        cur.execute(sql, answer)
        con.commit()
        return cur.lastrowid

    def get_id_value(self, id): 
        with self.connection as con:
            res = con.execute("SELECT * FROM wellbeing WHERE id = ?", (id,))
        return res 

    def get_all_values(self):
        with self.connection as con:
            res = con.execute("SELECT * FROM wellbeing")
            res = res.fetchall()
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
    
    def digital_twin_training(self):
        training_data = self.get_all_values()
        digital_twin = DigitalTwin(self.column_list)
        total_scores = digital_twin.total_scores(training_data)
        print(total_scores)
        self.construct_data_dictionary(total_scores[0], total_scores[1], total_scores[2])    
