from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bowrna'}
    posts = [
        {
            'author': {'username': 'Nithila'},
            'body': 'Beautiful day in Virudhunagar!'
        },
        {
            'author': {'username': 'Kannan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)