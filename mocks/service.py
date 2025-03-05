import requests

class APIClient:
    """A simple API client to get data"""
    def get_user_data(self,user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code != 200:
            raise ValueError(f"Unable to get user data for {user_id}")
        return response.json()

class UserService:
    """Uses API Client to fetch user data and process it"""
    def __init__(self,api_client):
        self.client = api_client

    def get_user_name(self,user_id):
        user_data = self.client.get_user_data(user_id)
        return user_data.get("name").upper()


