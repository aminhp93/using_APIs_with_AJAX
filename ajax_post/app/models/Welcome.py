""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Welcome(Model):
    def __init__(self):
        super(Welcome, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """

    def get_all_posts(self):
        query = "SELECT * FROM posts"
        return self.db.query_db(query)

    def create(self, post):
        query = "INSERT INTO posts (post, created_at) VAlues (:post, NOW())" 
        data = {'post': post['post']}
        return self.db.query_db(query, data)

    def get_last_post(self):
        query = "SELECT * FROM posts ORDER BY created_at DESC LIMIT 1"
        return self.db.query_db(query)