import gradio as gr
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app


def test_bot_query(mocker):
    """
    Test that a valid answer is received
    """
    message = "What's the weather like in Boulder?"
    history = []

    # Simulating answer
    mock_post = mocker.patch("app.requests.post")
    expected_response = {
        "data": {
            "flowise": """The weather in Boulder is currently cool
             with scattered clouds and high humidity."""
        }
    }
    mock_post.return_value.json.return_value = expected_response
    mock_post.return_value.status_code = 200  # simulate state code

    response = app.bot_query(message, history)

    assert response == expected_response["data"]["flowise"]
    mock_post.assert_called_once_with(
        "https://esthermariamh-graphql.hf.space/",
        json={
            "query": f"""
    query {{
        flowise(message: "{message}", history: {history})
    }}
    """
        },
    )


def test_bot_query_api_error(mocker):
    """
    Test a connection error is handled correctly
    """
    message = "Can I go shopping tomorrow, in Paris?"
    history = []

    mock_post = mocker.patch("app.requests.post")
    mock_post.side_effect = requests.exceptions.RequestException("API error")

    response = app.bot_query(message, history)

    assert (
        response
        == """Sorry, I can't connect to the server at the moment.
         Please try again later."""
    )


def test_check_auth(mocker):
    """
    Verify that the authentication is working properly
    """
    username = "testuser"
    password = "testpass"

    mock_client = mocker.patch("app.conectDB")
    mock_response = mocker.MagicMock()
    mock_response.data = [{"user": username, "password": password}]

    # Use variables to better code
    mock_table = mock_client.return_value.table.return_value
    mock_select = mock_table.select.return_value
    mock_eq1 = mock_select.eq.return_value
    mock_eq2 = mock_eq1.eq.return_value
    mock_execute = mock_eq2.execute.return_value

    # Final Value
    mock_execute.data = mock_response.data 

    assert app.check_auth(username, password) is True


def test_create_account(mocker):
    """
    Verifies that account creation works and handles errors
    """
    mocker.patch("app.conectDB", return_value=mocker.MagicMock())
    mock_db = app.conectDB()

    # Test successful account creation
    mock_db.table.return_value.insert.return_value.execute.return_value = None
    response = app.create_account("new_user", "password123")
    out = (
        "<h3 style='color: green;'>Account successfully created</h3>",
        "",
        "",
        "",
    )
    assert response == out

    # Test account creation with empty values
    response = app.create_account("", "")
    out = (
        "<h3 style='color: red;'>User name and password can't be empty.</h3>",
        "",
        "",
        "",
    )
    assert response == out


def test_delete_account(mocker):
    """
    Verifies that account deleting works and handles errors
    """
    mocker.patch("app.conectDB", return_value=mocker.MagicMock())
    mock_db = app.conectDB()

    # Test successful account deletion
    mock_table = mock_db.table.return_value
    mock_select = mock_table.select.return_value
    mock_eq1 = mock_select.eq.return_value
    mock_eq2 = mock_eq1.eq.return_value
    mock_execute = mock_eq2.execute.return_value
    mock_execute.data = [
        {"user": "test", "password": "test"}
    ]

    response = app.delete_account("test", "test", "test")
    expected_output = (
        "<h3 style='color: green;'>Account successfully deleted</h3>",
        "",
        "",
        "",
    )
    assert response == expected_output

    # Test account deletion for non-existing account
    mock_table = mock_db.table.return_value
    mock_select = mock_table.select.return_value
    mock_eq1 = mock_select.eq.return_value
    mock_eq2 = mock_eq1.eq.return_value
    mock_execute = mock_eq2.execute.return_value

    # value for non existing account
    mock_execute.data = []

    response = app.delete_account("wrong_user", "wrong_pword", "wrong_pword")
    expected_output = (
        "<h3 style='color: red;'>You wrote a wrong password or account.</h3>",
        "",
        "",
        "",
    )
    assert response == expected_output


def test_login(mocker):
    """
    Test for the login function
    """
    mocker.patch("app.check_auth", return_value=True)
    response = app.login("test", "test")
    assert response == (
        "",
        gr.update(visible=False),
        gr.update(visible=True),
        "",
        "",
        "",
    )

    mocker.patch("app.check_auth", return_value=False)
    response = app.login("wrong_user", "wrong_password")
    expected_output = ("<h3 style='color: red;'>"
                       "Invalid username or password.</h3>"
                       )
    assert response == (
        expected_output,
        gr.update(visible=True),
        gr.update(visible=False),
        "",
        "",
        "",
    )
    
