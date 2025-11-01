# models/user.py
users = []  # Simulación de base de datos en memoria
id_counter = 1

class User:
    def __init__(self, name, email):
        global id_counter
        self.id = id_counter
        self.name = name
        self.email = email
        id_counter += 1

    @staticmethod
    def get_all():
        return users

    @staticmethod
    def get_by_id(user_id):
        return next((u for u in users if u.id == user_id), None)

    @staticmethod
    def create(name, email):
        user = User(name, email)
        users.append(user)
        return user

    @staticmethod
    def update(user_id, name, email):
        user = User.get_by_id(user_id)
        if user:
            user.name = name
            user.email = email
        return user

    @staticmethod
    def delete(user_id):
        global users
        user = User.get_by_id(user_id)
        if user:
            users = [u for u in users if u.id != user_id]
            return True
        return False