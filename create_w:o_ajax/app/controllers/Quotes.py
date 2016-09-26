from system.core.controller import *
class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('Quote')
    def index(self):
        quotes = self.models['Quote'].all();
        return self.load_view('quotes/index.html', quotes = quotes)
    # def index_json(self):
    #     quotes = self.models['Quote'].all()
    #     return jsonify(quotes=quotes)

    # def index_html(self):
    # 	quotes = self.models['Quote'].all()
    # 	return self.load_view('partial/quotes.html', quotes = quotes)

    def create(self):
        new_quote = {'author': request.form['author'], 'quote': request.form['quote']}
        self.models['Quote'].create(new_quote)

        quotes = self.models['Quote'].all();
        return self.load_view('partial/quotes.html', quotes = quotes)

