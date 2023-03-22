#!/usr/bin/python3
"""Flask app with four routes."""


from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'} \ 
, methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python(text):
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
