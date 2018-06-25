# Main server
from flask import Flask, request, Response, jsonify, render_template

app = Flask(__name__)

# The basic viewing route
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-random-word', methods=['GET'])
def random_word():
	# @param base_lang: base language in which this word should be
	# return a random word (with meaning) as a dictionary
  return jsonify({
  	'word' : 'bonjour',
  	'meaning' : 'Good day!'
  })

if __name__ == "__main__":
	app.run(debug=True)