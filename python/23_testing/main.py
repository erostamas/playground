import requests

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()



import pytest
from unittest.mock import patch
#from my_module import get_user_data

# Fixture to provide a mocked response JSON
@pytest.fixture
def mock_user_data():
    return {"id": 123, "name": "Alice"}

def test_get_user_data(mock_user_data):
    with patch('requests.get') as mock_get:
        # Configure the mock to return a response with our mock_user_data JSON
        mock_get.return_value.json.return_value = mock_user_data

        # Call the function — it will use the mocked requests.get
        result = get_user_data(123)

        # Assert the function returns our mocked data
        assert result == mock_user_data

        # Optional: assert the URL was called correctly
        mock_get.assert_called_once_with("https://api.example.com/users/123")


"""
mock db access
with patch('myapp.db.get_user') as mock_get_user:
    mock_get_user.return_value = {'id': 1, 'name': 'Alice'}

mock date and time
with patch('datetime.datetime') as mock_datetime:
    mock_datetime.now.return_value = datetime.datetime(2020, 1, 1)

mock file open without touching the disk
mocked_file = mock_open(read_data="file contents")
with patch('builtins.open', mocked_file):
    with open('dummy.txt') as f:
        content = f.read()
    assert content == "file contents"
    
mock entire classes
with patch('module.ClassName') as MockClass:
    instance = MockClass.return_value
    instance.method.return_value = 'mocked result'

skip sleeps
with patch('time.sleep', return_value=None):
    # Code calling sleep will return immediately
"""


"""
Name	Purpose	Behavior
Dummy	Passed around but never used	Just a placeholder (e.g., None or empty object)
Fake	Has a working implementation but simplified	Realistic but simpler version of real code (e.g., in-memory DB)
Stub	Provides predefined responses	Returns canned responses to calls, doesn’t respond dynamically
Spy	Records information about calls	Like a mock but mainly to verify interactions (calls, args)
Mock	Pre-programmed with expectations	Verifies interactions, can fail tests if expectations not met
"""


"""
parametrized tests
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input * input == expected
"""