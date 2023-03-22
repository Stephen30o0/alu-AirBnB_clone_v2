#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    """Displays a HTML page like 6-index.html"""
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           all_states=all_states,
                           all_amenities=all_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
