from models import User


class Admin(User):
    def __init__(self, us, pw, em, permission):
        super().__init__(us, pw, em)
        self.permission = permission

    def kick(self, username):
        print(f"user {username} was kicked")


shayan = Admin("Shayan123", "@456", "shayan@gmail.com", True)
shayan.kick("parsa")
