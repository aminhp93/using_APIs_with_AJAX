from system.core.model import Model
class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()
    def all(self):
        query = "SELECT * FROM quotes"
        return self.db.query_db(query)