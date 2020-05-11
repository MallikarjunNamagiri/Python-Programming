'''
set the Flask environment in windows: set FLASK_APP=Flaskblog.py
Run the Flask web application		: flask run
Server show changes without restrat	: set FLASK_DEBUG=1
'''

from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECURITY KEY'] = 'bf22c5e81e14f93cd7b1daefce2e9f39'

# import secrets
# secrets.token_hex(16)

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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# flask run directly from the code
if __name__ == '__main__':
	app.run(debug=True)
