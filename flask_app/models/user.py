from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (name) VALUES (%(name)s);"
        return connectToMySQL(DB).query_db(query,data)