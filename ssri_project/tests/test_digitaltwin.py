from src.digitaltwin import DigitalTwin
import pytest
from unittest.mock import MagicMock,Mock, patch

model = DigitalTwin(["question1", "question2", "question3", "question4", "question5","question6,","question7",
        "question8", "question9", "question10", "question11", "question12", "question13", "question14"])  # Assuming this is correct

@pytest.fixture
def drug_citalopram():
    return "Citalopram"

@pytest.fixture
def drug_sertraline():
    return "Sertraline"

@pytest.fixture
def drug_fluoxetine():
    return "Fluoxetine"

@pytest.fixture
def drug_none():
    return "None"

def test_decide_colours_citalopram(): 
    colour = model.decide_colours("Citalopram")
    assert colour == "magenta"

def test_decide_colours_fluoxetine(): 
    colour = model.decide_colours("Fluoxetine")
    assert colour == "red"

def test_decide_colours_sertraline(): 
    colour = model.decide_colours("Sertraline")
    assert colour == "blue"

def test_decide_colours_none(): 
    colour = model.decide_colours("None")
    assert colour == "green"

def test_decide_colours_case():
    colour = model.decide_colours("citalopram")
    assert colour == "magenta"

def test_decide_colours_empty_string():
    colour = model.decide_colours("")
    assert colour == "red"

# def test_total_scores_none():
#     total_scores = model.total_scores({'id': None, 'user_id': None, 'date': None, 'antidepressant': None})
#     assert total_scores == {'None': [(None, None)]}

def test_total_scores_return_length():
    training_data = [{'id': 26, 'user_id': 19, 'date': '2023-04-17', 'antidepressant': 'Citalopram', 'question1': 1, 'question2': 1, 'question3': 1, 'question4': 2, 'question5': 2, 'question6': 1, 'question7': 1, 'question8': 1, 'question9': 1, 'question10': 1, 'question11': 1, 'question12': 1, 'question13': 1, 'question14': 1}, {'id': 27, 'user_id': 19, 'date': '2023-04-24', 'antidepressant': 'Citalopram', 'question1': 3, 'question2': 3, 'question3': 3, 'question4': 3, 'question5': 3, 'question6': 3, 'question7': 3, 'question8': 3, 'question9': 3, 'question10': 3, 'question11': 3, 'question12': 3, 'question13': 3, 'question14': 3}]
    result = model.total_scores(training_data)
    assert len(result[0]) == len(result[1]) == len(result[2])

def test_total_scores_output():
    training_data = [{'id': 26, 'user_id': 19, 'date': '2023-04-17', 'antidepressant': 'Citalopram', 'question1': 1, 'question2': 1, 'question3': 1, 'question4': 2, 'question5': 2, 'question6': 1, 'question7': 1, 'question8': 1, 'question9': 1, 'question10': 1, 'question11': 1, 'question12': 1, 'question13': 1, 'question14': 1}, {'id': 27, 'user_id': 19, 'date': '2023-04-24', 'antidepressant': 'Citalopram', 'question1': 3, 'question2': 3, 'question3': 3, 'question4': 3, 'question5': 3, 'question6': 3, 'question7': 3, 'question8': 3, 'question9': 3, 'question10': 3, 'question11': 3, 'question12': 3, 'question13': 3, 'question14': 3}]
    result = model.total_scores(training_data)
    assert result[0] == ['Citalopram', 'Citalopram']
    assert result[1] == [1, 3]
    assert result[2] == ['2023-04-17', '2023-04-24']
    