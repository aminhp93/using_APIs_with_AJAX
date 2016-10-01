"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Note')
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
        notes = self.models['Note'].get_all_notes()
        return self.load_view('index.html', notes = notes)

    def create(self):
        note = {'title': request.form['title'], 'description': request.form['description']}
        id = self.models['Note'].create(note)
        
        note = self.models['Note'].get_note_by_id(id)
        return self.load_view('partials/notes.html', note = note[0])

    def update(self):
        note = {'id': request.form['id'], 'description': request.form['description']}
        self.models['Note'].update(note)

        note = self.models['Note'].get_note_by_id(request.form['id'])
        return self.load_view('partials/update.html', note = note[0])

    def delete(self):
        id = request.form['id']

        note = self.models['Note'].get_note_by_id(id)
        return self.load_view('partials/notes.html', note = note[0])



