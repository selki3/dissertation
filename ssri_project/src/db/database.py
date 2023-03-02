import sqlite3

con = sqlite3.connect("db/antidepressant.db")
cur = con.cursor()

# Create columns needed in one table
# date being text so its stored as an ISO8601 string
# date YYYY-MM-DD HH:MM:SS.SSS
wellbeing_table = """
    CREATE TABLE IF NOT EXISTS wellbeing ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    date TEXT NOT NULL,
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
    question14 INTEGER NOT NULL
)"""

cur.execute(wellbeing_table)

# Input placeholder values
# Not committing right now 
wellbeing_sql = "INSERT INTO wellbeing (id, date, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) VALUES (2, '2023-01-28 23:59:00.000', 1, 2, 3, 4, 5, 1, 2, 2, 3, 1, 4, 4, 5, 4)"
wellbeing_sql = "INSERT INTO wellbeing (id, date, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14) VALUES (1, '2023-01-26 23:59:00.000', 1, 1, 3, 4, 5, 1, 2, 2, 3, 4, 2, 1, 1, 2)"

cur.execute(wellbeing_sql)

cur.execute("SELECT * FROM wellbeing")
for row in cur:
  print(row)