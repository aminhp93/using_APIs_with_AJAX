"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcomes(Controller):
    def __init__(self, action):
        super(Welcomes, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Welcome')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)

        """
        posts = self.models['Welcome'].get_all_posts()
        return self.load_view('index.html', posts = posts)

    def create(self):
        result = {'post': request.form['post']}
        self.models['Welcome'].create(result)

        post = self.models['Welcome'].get_last_post()

        return self.load_view('partials/posts.html', post = post[0])

    # def index_json(self):
    #     quotes = self.models['Welcome'].get_all_posts()
    #     return jsonify(quotes = quotes)
