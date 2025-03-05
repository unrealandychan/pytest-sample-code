from service import UserService , APIClient
import pytest

def test_get_user_name(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)

    mock_api_client.get_user_data.return_value = {"id":1,"name": "eddie"}

    service = UserService(mock_api_client)
    result = service.get_user_name(1)

    # Assertions
    assert result == "EDDIE"
    mock_api_client.get_user_data.assert_called_once_with(1)