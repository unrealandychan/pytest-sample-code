import pytest
from get_data import get_weather

def test_get_weather(mocker):
    # Mocking the requests.get function
    mock_get = mocker.patch("get_data.requests.get")

    # Mocking the return value of the requests.get function
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temp": 21}

    # Call function
    result = get_weather("London")

    # Assertions
    assert result == {"temp": 21}
    mock_get.assert_called_once_with("https://api.weather.com/v1/London")