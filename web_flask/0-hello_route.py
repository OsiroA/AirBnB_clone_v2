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


if __name__ == '__main__':
    oosi.run(host='0.0.0.0', port=5000)
