#!/usr/bin/python3
"""Flask app with six routes."""


from flask import Flask, render_template
from markupsafe import Markup

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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    n = Markup.escape(n)
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
