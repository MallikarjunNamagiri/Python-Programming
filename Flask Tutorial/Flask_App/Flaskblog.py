'''
set the Flask environment in windows: set FLASK_APP=Flaskblog.py
Run the Flask web application		: flask run
Server show changes without restrat	: set FLASK_DEBUG=1
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home Web Page</h1>"

@app.route('/about')
def hello():
	return "<h2>About Page</h2>"

# flask run directly from the code
if __name__ == '__main__':
	app.run(debug=True)