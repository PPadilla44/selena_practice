from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import attraction

class Location:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.attractions = []


        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM locations"
        results = connectToMySQL(DB).query_db(query)
        locations = []
        for location in results:
            locations.append(cls(location))
        return locations

    @classmethod
    def get_all_joined(cls, data):
        query = "SELECT * FROM locations LEFT JOIN attractions ON attractions.locations_id = locations.id WHERE locations.id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        location = cls(results[0])
        for row in results:
            attr_data = {
                "id": row['attractions.id'],
                "name": row['attractions.name'],
                "created_at": row['attractions.created_at'],
                "updated_at": row['attractions.updated_at'],
                "locations_id": row['id']
            }
            location.attractions.append(attraction.Attraction(attr_data))

        return location


    @classmethod
    def save(cls,data):
        query = "INSERT INTO locations (name, users_id) VALUES (%(name)s, %(users_id)s);"
        return connectToMySQL(DB).query_db(query,data)