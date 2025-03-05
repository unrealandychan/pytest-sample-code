class UserManager:
    def __init__(self):
        self.user = {}

    def add_user(self,username,email):
        if username in self.user:
            raise ValueError("Username already exists")
        self.user[username] = email
        return True

    def get_user_by_username(self,username):
        return self.user.get(username)