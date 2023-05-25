from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import sqlite3 
from sqlite3 import Error, IntegrityError
import bcrypt

from .digitaltwin import DigitalTwin

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
        if username == "": 
            raise ValueError("Usernames cannot be blank. Try again.")
        if password == "": 
            raise ValueError("Passwords cannot be blank. Try again.")

        password = password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=4)
        hashed = bcrypt.hashpw(password, salt)
        
        with self.connection as con:
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO user(username, password) VALUES(?, ?)", (username, hashed))
                con.commit()
                return True
            except IntegrityError as e: 
                print("There is a duplicate username! Please try again.")
    
    def login(self, username, password):
        with self.connection as con:
            cur = con.cursor()
            cur.execute("SELECT password FROM user WHERE username = ?", (username,))
            actual_password = cur.fetchone()
            if actual_password is not None:
                actual_password = list(actual_password.values())[0]
                password = password.encode('utf-8')
                if (bcrypt.checkpw(password, actual_password)):
                    print("Logged in")
                    cur.execute("SELECT id FROM user WHERE username = ?", (username,))
                    return cur.fetchone()
                if not (bcrypt.checkpw(password, actual_password)):
                    raise ValueError("The login details are incorrect. Please try again.")
        return None
