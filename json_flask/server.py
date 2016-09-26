from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'myownapi')

@app.route('/quotes')
def index():
	return render_template('index.html')

@app.route('/quotes/index_json')
def index_json():
	query = "SELECT * FROM quotes"
	quotes = mysql.query_db(query)
	print quotes
	return jsonify(quotes = quotes)

app.run(debug=True)