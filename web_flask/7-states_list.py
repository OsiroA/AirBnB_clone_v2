#!/usr/bin/python3
"""
This starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

oosi = Flask(__name__)


@oosi.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@oosi.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    oosi.run(host="0.0.0.0", port=5000)
