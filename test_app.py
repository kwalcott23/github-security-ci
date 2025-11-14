import pytest
from app import add, subtract, get_data
import requests # <-- Added this import to access requests.exceptions

# Simple tests for basic arithmetic
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    assert subtract(5, 5) == 0

# Test for the function using the 'requests' dependency
def test_get_data_mock_success(monkeypatch):
    # Mock the requests.get method to return a successful response
    class MockResponse:
        status_code = 200
        def raise_for_status(self):
            pass  # Simulate no HTTP errors
    
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    result = get_data("http://mockurl.com")
    assert "Successfully fetched" in result

def test_get_data_mock_failure(monkeypatch):
    # Mock the requests.get method to raise an exception
    def mock_get_error(*args, **kwargs):
        # FIX: We must raise the exception instance directly, 
        # not use pytest.raises(). We use RequestException because 
        # app.py catches it.
        raise requests.exceptions.RequestException("Connection error")

    monkeypatch.setattr("requests.get", mock_get_error)
    result = get_data("http://errorurl.com")
    assert "Request failed" in result
