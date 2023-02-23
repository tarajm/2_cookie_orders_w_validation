from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie_order:

    db = 'cookie_order'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#IS VALID METHOD - to check if the users' input meets the requirements
#use a static method  - if you use a static method you can only pass in one parameter (data)
    @staticmethod
    def is_valid(data):
        valid = True
        #now create gloabl if check to address that all boxes are not left blank

        if len(data['name']) <= 0 or len(data['cookie_type']) <= 0 or len(data['num_of_boxes']) <= 0:
            valid = False
            flash("All fields are required!")
            return valid
        
        #now create checks to make sure name and cookie type are a minimum of 2 characters
        if len(data['name']) < 2:
            valid = False
            flash("Name must be at least 2 characters!")
        if len(data['cookie_type']) <2:
            valid = False
            flash("Cookie Type my be at least characters!")
        
        #now create a check to make sure the num_of_boxes is NOT negative
        if len(data['num_of_boxes']) < 0:
            valid = False
            flash("Please enter a valid number of boxes!  Cannot be negative!")
        return valid





##anytime the TABLE order is referenced....replace it with cookie_order.order

#create CRUD method

#READ ALL (GET ALL)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_order.order;"
        results = connectToMySQL(cls.db).query_db(query)
        orders = []
        for row in results:
            orders.append(cls(row))
        return orders
        


#READ ONE (GET ONE) - GET BY ID
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM cookie_order.order WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        # data = {
        #     "id" : id
        # }
        # results = connectToMySQL(cls.db).query_db(query, data)
        # if results:
        #     order = results[0]
        #     return order
        return cls(results[0])
    

#CREATE/SAVE METHOD

    @classmethod
    def create(cls, data):
        query = "INSERT into cookie_order.order (name, cookie_type, num_of_boxes) VALUES ( %(name)s, %(cookie_type)s, %(num_of_boxes)s );"
        return connectToMySQL(cls.db).query_db(query, data)


#UPDATE/EDIT METHOD

    @classmethod
    def update(cls, data):
        query = "UPDATE cookie_order.order SET name = %(name)s, cookie_type = %(cookie_type)s, num_of_boxes = %(num_of_boxes)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result


#Delete Method
    @classmethod
    def delete(cls, data):
        pass



        


