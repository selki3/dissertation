from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import sqlite3 
from sqlite3 import Error
from digitaltwin import DigitalTwin
import bcrypt

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

# Represents the table of data 
class UserModel(QtCore.QAbstractListModel):
    def __init__(self, *args, question=None, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)
        self.connection = self.create_connection()

    def create_connection(self): 
        con = None
        try:
            con = sqlite3.connect("db/antidepressant.db")
        except Error as e:
            print(e)
        else:
            con.row_factory = dict_factory
            return con
    
    def create_user(self, username, password):
        password = password.encode()
        salt = bcrypt.gensalt(rounds=4)
        hashed = bcrypt.hashpw(password, salt)

        with self.connection as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user(username, password) VALUES(?, ?)", (username, hashed))
            con.commit()
    
    def login(self, username, password):
        password = password.encode()
        salt = bcrypt.gensalt(rounds=4)
        hashed = bcrypt.hashpw(password, salt)

        with self.connection as con:
            cur = con.cursor()
            cur.execute("SELECT password FROM user WHERE username = ?", (username))
            actual_password = cur.fetchone()[0]

            if actual_password == password:
                print("Logged in")
                return True
            else:
                print("Failed")
            

