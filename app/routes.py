from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'virekuma'}
    posts = [
        {
            'author': {'username': 'lovee'},
            'body': 'Pune is beautiful place'
        },
        {
            'author': {'username': 'rahul'},
            'body': 'I live in Aligarh'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
