class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username


user_1 = User("001", "test1")
user_2 = User("002", "test2")

print(user_1.id)
