#!/usr/bin/python3
"""
This is a script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

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


@oosi.route('/python/', strict_slashes=False)
@oosi.route('/python/<text>', strict_slashes=False)
def pythonRoute(text="is cool"):
    '''
    This function replaces a given text
    '''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@oosi.route('/number/<int:n>', strict_slashes=False)
def numberRoute(n):
    '''
    This displays the value [passed into the function
    only if it is an integer
    '''
    return "{} is a number".format(n)
    '''
    except ValueError:
        return "N no be number"
    '''


@oosi.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    '''This function displays an HTML page only oif n is an integer'''
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    oosi.run(host='0.0.0.0', port=5000)
