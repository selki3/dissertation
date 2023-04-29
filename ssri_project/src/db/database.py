import sqlite3

con = sqlite3.connect("antidepressant.db")
cur = con.cursor()

user_table = """
    CREATE TABLE IF NOT EXISTS user ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)"""

cur.execute(user_table)

# Create columns needed in one table
# date being text so its stored as an ISO8601 string
# date YYYY-MM-DD HH:MM:SS.SSS
wellbeing_table = """
    CREATE TABLE IF NOT EXISTS wellbeing ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    antidepressant TEXT NOT NULL,
    question1 INTEGER NOT NULL,
    question2 INTEGER NOT NULL, 
    question3 INTEGER NOT NULL,
    question4 INTEGER NOT NULL,
    question5 INTEGER NOT NULL,
    question6 INTEGER NOT NULL,
    question7 INTEGER NOT NULL,
    question8 INTEGER NOT NULL,
    question9 INTEGER NOT NULL,
    question10 INTEGER NOT NULL,
    question11 INTEGER NOT NULL,
    question12 INTEGER NOT NULL, 
    question13 INTEGER NOT NULL, 
    question14 INTEGER NOT NULL,
    FOREIGN KEY (user_id)
    REFERENCES user(id)
)"""

cur.execute(wellbeing_table)


# Input placeholder values
# Not committing right now 
user_sql = "INSERT INTO user (id, username, password) VALUES (1, 'username', 'password')"

cur.execute(user_sql)

wellbeing_sql = "INSERT INTO wellbeing (id, user_id, date, antidepressant, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) VALUES (1, 1, '2023-01-22', 'citalopram', 1, 2, 3, 4, 5, 1, 2, 2, 3, 1, 4, 4, 5, 4)"

cur.execute(wellbeing_sql)

wellbeing_sql = "INSERT INTO wellbeing (id, user_id, date, antidepressant, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) VALUES (2, 1, '2023-01-28', 'citalopram', 1, 2, 3, 4, 5, 1, 2, 2, 3, 1, 4, 4, 5, 4)"

cur.execute(wellbeing_sql)


cur.execute("SELECT * FROM wellbeing")
for row in cur:
      print(row)


cur.execute("SELECT * FROM user")
for row in cur:
  print(row)

con.commit()
