### Main server
# Imports
from flask import Flask, request, Response, jsonify, render_template
from flask_pymongo import PyMongo
from util import *

# Setup
ENVIRONMENT = readenv()

app = Flask(__name__)
app.config['MONGO_HOST'] = ENVIRONMENT['MONGO_HOST']
app.config['MONGO_DBNAME'] = ENVIRONMENT['MONGO_DBNAME']
mongo = PyMongo(app)

# The basic viewing route
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-random-word', methods=['GET'])
def random_word():
	# @param base_lang: base language in which this word should be
	#
	# return a random word (with meaning) as a dictionary
  return jsonify({
  	'word' : 'bonjour',
  	'meaning' : 'Good day!'
  })

@app.route('/insert-word', methods=['GET'])
def insert_word():
	# @param word: the new word learned
	# @param language: which language this word is in
	# @param meaning: the meaning of this word
	#
	# insert a new word in the db
	word = request.args.get('word')
	language = request.args.get('language')
	meaning = request.args.get('meaning')

	try:
		mongo.db[language].insert_one({
			'word': word,
			'meaning': meaning
		})
		return jsonify({'success':True})
	except e:
		return jsonify({'exception' : e, 'success':False})

if __name__ == "__main__":
	app.run(debug=True)