from src.information_processor import QuestionModel
import pytest
from unittest.mock import MagicMock,Mock, patch
import datetime as dt 


@pytest.fixture
def questions():
    return QuestionModel(question = "I am feeling optimistic about the future")

def test_data(questions):
    actual = questions.data()
    assert actual == questions.question

def test_connection_successful(questions):
    mock_con = MagicMock()
    with patch('sqlite3.connect', mock_con):
        con = questions.create_connection()
        assert mock_con.called_with('db/antidepressant.db')

def test_get_all_values(questions):
    today = dt.date.today().strftime('%Y-%m-%d')
    test_data = (today, "citalopram", 1,1,1,1,1,1,1,1,1,1,1,1,1,1)
    with questions.connection as con:
        cur = con.execute("""
            INSERT INTO wellbeing(
                user_id, date, antidepressant, question1, question2, 
                question3, question4, question5, question6, question7,
                question8, question9, question10, question11, question12,
                question13, question14
            ) 
            VALUES(1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, test_data)
        inserted_id = cur.lastrowid
        con.commit()

    fetched_data = questions.get_all_values(1)
    retrieved_data = {'id': inserted_id, 'user_id': 1, 'date': '2023-06-05', 'antidepressant': 'citalopram', 'question1': 1, 'question2': 1, 'question3': 1, 'question4': 1, 'question5': 1, 'question6': 1, 'question7': 1, 'question8': 1, 'question9': 1, 'question10': 1, 'question11': 1, 'question12': 1, 'question13': 1, 'question14': 1}
    assert retrieved_data in list(fetched_data)
