from src.information_processor import QuestionModel
import pytest
from unittest.mock import MagicMock,Mock, patch

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


