# Main server
from flask import Flask, request, Response, jsonify, render_template

app = Flask(__name__)

# The basic viewing route
@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)