"""
Linnworks API authentication
"""

import requests


APPLICATION_ID = None
APPLICATION_SECRET = None
TOKEN = None


def set_application_id(application_id):
    """Sets the application ID value.

    Args:
        application_id (str): The application ID.
    """

    global APPLICATION_ID
    APPLICATION_ID = application_id


def set_application_secret(application_secret):
    """Sets the application secret value.

    Args:
        application_secret (str): The application secret.
    """

    global APPLICATION_SECRET
    APPLICATION_SECRET = application_secret


def set_token(token):
    """Sets the token value.

    Args:
        token (str): The token.
    """

    global TOKEN
    TOKEN = token


def get_application_id():
    """Gets the application ID value.

    Returns:
        str: The application ID.
    """

    return APPLICATION_ID


def get_application_secret():
    """Gets the application secret value.

    Returns:
        str: The application secret.
    """

    return APPLICATION_SECRET


def get_token():
    """Gets the token value.

    Returns:
        str: The token.
    """

    return TOKEN


def authenticate():
    """Use Requests to query the Linnworks API and retrieve the Token."""

    payload = {
        'applicationId': APPLICATION_ID,
        'applicationSecret': APPLICATION_SECRET,
        'Token': TOKEN
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(
            url="https://api.linnworks.net/api/Auth/AuthorizeByApplication",
            data=payload,
            headers=headers)
        return response.json()['Token']
    except Exception as e:
        print('Failed to get token. Check your credentials are correct.')
        exit()

