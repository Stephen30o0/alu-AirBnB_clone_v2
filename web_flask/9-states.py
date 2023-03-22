#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all State objects."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """Display a HTML page with a list of all City objects in a State."""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', id=id, not_found=True)
    sorted_cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=sorted_cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
