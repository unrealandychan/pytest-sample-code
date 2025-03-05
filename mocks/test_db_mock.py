from db import save_user
def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("eddie", 25)

    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with("INSERT INTO users VALUES (?,?)", ("eddie", 25))