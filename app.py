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
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# The basic viewing route
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-random-word', methods=['GET'])
def random_word():
	# @param language: base language in which this word should be
	#
	# return a random word (with meaning) as a dictionary
	language = request.args.get('input_language')

	query = mongo.db[language].aggregate(
  		[{'$sample': { 'size': 1 }}]
		)
	random_doc = query.next()
	return jsonify({
		'word': random_doc['word'],
		'meaning': random_doc['meaning']
	})

@app.route('/insert-word', methods=['GET'])
def insert_word():
	# @param word: the new word learned
	# @param language: which language this word is in
	# @param meaning: the meaning of this word
	#
	# insert a new word in the db, ONLY if the user has
	# entered the correct 'secret' word
	word = request.args.get('input_word')
	language = request.args.get('input_language')
	meaning = request.args.get('input_meaning')
	secret = request.args.get('input_secret')

	# check if the secret is correct
	if (secret != ENVIRONMENT['INSERT_SECRET']):
		print ("The secret was incorrect!")
		return jsonify({"success": False})

	try:
		mongo.db[language].insert_one({
			'word': word,
			'meaning': meaning
		})
		return jsonify({'success':True})
	except Exception as e:
		return jsonify({'exception' : str(e), 'success':False})

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)