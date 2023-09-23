#!/usr/bin/python3
"""
This is a script that starts a Flask web application
"""
from flask import Flask


oosi = Flask(__name__)


@oosi.route('/', strict_slashes=False)
def hello():
    """
    This function returns a requested string
    """
    return 'Hello HBNB!'


@oosi.route('/hbnb', strict_slashes=False)
def helloHbnb():
    """
    This function displays just HBNB
    """
    return 'HBNB'


@oosi.route('/c/<text>', strict_slashes=False)
def cRoute(text):
    '''
    this displays C followed by the value of
    the text variable
    '''
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    oosi.run(host='0.0.0.0', port=5000)
