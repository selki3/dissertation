from src.QuestionController import QuestionController
import pytest
from unittest.mock import MagicMock,Mock, patch

@pytest.fixture
def questions():
    return QuestionController(14, "Citalopram")  # Assuming this is correc

def test_extract_information_none(questions):
    actual = questions.extract_information(None, 4)
    assert actual is None 

def test_extract_information_id(questions):
    # Will be none because of answers
    id = 2
    question_id = 14 
    actual = questions.extract_information(id, question_id)
    assert actual == id

def test_change_medication(questions):
    medication = "Sertraline"
    questions.change_medication(medication)
    assert questions.medication == medication

def test_construct_dictionary(questions):
    id = 4
    question_id = 1
    actual = questions.extract_information(id, question_id)
    dictionary = questions.construct_dictionary()
    assert id in dictionary 
    
