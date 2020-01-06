from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    # return "Hello, World"
    user = {'username': 'virekuma'}
    # return """
    # <html>
    #     <head>
    #         <title>Microblog</title>
    #     </head>
    #     <body>
    #         <h1>Hi, """ + user['username'] + """</h1>
    #     </body>
    # </html>
    # """
    return render_template('index.html', title='Home', user=user)
