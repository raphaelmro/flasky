from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'Your browser is {user_agent}'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello World, {name}!</h1>'
