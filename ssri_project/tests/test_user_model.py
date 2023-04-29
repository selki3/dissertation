import pytest
from unittest.mock import MagicMock,Mock, patch

from src.user_model import UserModel

user = UserModel()  # Assuming this is correct

def test_create_user_username_exception():
    expected = "Usernames and passwords cannot be blank"

    with pytest.raises(ValueError) as exception_context:
        user.create_user("", "")
        assert str(exception_context.exception) == expected
        
def test_create_user_duplicate_username_exception(): 
    expected = "There is a duplicate username! Please try again."
        # Under the assumption that when the DB is created, username and password is there
    with pytest.raises(ValueError) as exception_context:
        user.create_user("username", "")
        assert str(exception_context.exception) == expected

def test_login_user_incorrect_exception():
    username = ("username").encode("utf-8")
    password = ("invalid").encode("utf-8")
    actual = user.login(username, password)
    assert actual is None
    
def test_connection_successful():
    mock_con = MagicMock()
    with patch('sqlite3.connect', mock_con):
        con = user.create_connection()
        assert mock_con.called_with('db/antidepressant.db')
