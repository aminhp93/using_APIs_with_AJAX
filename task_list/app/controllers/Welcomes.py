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
        tasks = self.models['Welcome'].get_all_tasks()
        return self.load_view('index.html', tasks = tasks)

    def create(self):
        result = {'task': request.form['task']}
        self.models['Welcome'].create(result)

        task = self.models['Welcome'].get_last_task()

        return self.load_view('partials/tasks.html', task = task[0])

    # def index_json(self):
    #     quotes = self.models['Welcome'].get_all_posts()
    #     return jsonify(quotes = quotes)
    def edit(self, id):
        task = self.models['Welcome'].get_task_by_id(id)
        return self.load_view('partials/tasks.html', task = task[0])