from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import sqlite3 
from sqlite3 import Error

# Represents the table of data 
class QuestionModel(QtCore.QAbstractListModel):
    def __init__(self, *args, question=None, **kwargs):
        super(QuestionModel, self).__init__(*args, **kwargs)
        self.connection = create_connection()
        self.question = question 

    def data(self):
        return self.question

    def rowCount(self, index):
        return len(self.question)

    def create_connection(self): 
        con = None
        try:
            con = sqlite3.connect("antidepressant.db")
        except Error as e:
            print(e)
        return con

    def create_answer(self, con, answer):
        sql = '''INSERT INTO wellbeing(date, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cur = con.cursor()
        print(answer)
        cur.execute(sql, answer)
        con.commit()
        return cur.lastrowid

    def get_id_value(self, id): 
        with self.connection as con:
            res = con.execute("SELECT * FROM wellbeing WHERE id = ?")
            
    def get_all_values(self):
        with self.connection as con:
            res = con.execute("SELECT * FROM wellbeing")
            res = fetchall()
        return res 
    
    
    
