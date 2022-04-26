from flask import request
from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL


class Attraction:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.locations_id = data['locations_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM attractions"
        results = connectToMySQL(DB).query_db(query)
        attractions = []
        for attraction in results:
            attractions.append(cls(attraction))
        return attractions


    @classmethod
    def save_mult(cls, data, loc_id):
        newData = {
            **request.form,
            "morelines": cls.add_more_values(data, loc_id)
        }
        test = cls.add_more_values(data, loc_id)
        query = f"INSERT INTO attractions (name, locations_id) VALUES {test};"
        return connectToMySQL(DB).query_db(query,newData)
    

    @staticmethod
    def add_more_values(data, loc_id):
        more_values_str = ""
        results = data.to_dict(flat=False)
        for i, name in enumerate(results['name']):
            if i == len(results['name']) - 1:
                more_values_str += f"('{name}', {loc_id})"
            else:
                more_values_str += f"('{name}', {loc_id}), "

        return more_values_str
