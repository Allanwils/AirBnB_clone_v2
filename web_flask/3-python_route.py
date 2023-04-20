#!/usr/bin/python3
"""
This script initializes a Flask web application and sets up several routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Displays "Hello HBNB!" when accessing the root path.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when accessing the /hbnb path.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Displays "C ", followed by the value of the text variable (replace underscores with spaces),
    when accessing the /c/<text> path.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Displays "Python ", followed by the value of the text variable (replace underscores with spaces),
    when accessing the /python/<text> path. If <text> is not provided, displays "Python is cool".
    """
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
