'''
set the Flask environment in windows: set FLASK_APP=Flaskblog.py
Run the Flask web application		: flask run
Server show changes without restrat	: set FLASK_DEBUG=1
'''

from flask import Flask, render_template
app = Flask(__name__)

#dummpy data
posts = [
    {
        'author': 'Malli Namagiri', 
        'title': 'Blog Post-1',
        'content': 'First post content',
        'date_posted': 'April 06, 2020'
    },
    {
        'author': 'Khailash Namagiri', 
        'title': 'Blog Post-2',
        'content': 'Second post content',
        'date_posted': 'April 07, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    #return "<h1>Home Web Page</h1>"
    return render_template('home.html', posts=posts)

@app.route('/about')
def hello():
	return render_template('about.html', title='About')

# flask run directly from the code
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')