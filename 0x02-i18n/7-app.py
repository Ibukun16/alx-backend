#!/usr/bin/env python3
"""A basic flask app that mimick
creating a user login system
"""
import pytz
from flask_babel import Babel
from typing import Union, Dict
from os import getenv
from flask import Flask, render_template, request, g


class Config(object):
    """Flask babel configuration

    Return:
            _type_: _description_
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get a user based on the user id and return a dictionary of the
    user details or None if the ID cannot be found

    Return:
            _type_: _description_(the user id or None)
    """
    user_id = request.args.get('login_as', '')
    if user_id:
        return users.get(int(user_id, None))
    return None


@app.before_request
def before_request() -> None:
    """
    Perform some routine tasks before the resolution of each request
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Get the locale for a webpage

    Return:
            _type_: _description - Webpage
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        print(locale)
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """Get the timezone of the location of a webpage"""
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """Use get_index to retrieve index as homepage

    Return:
            _type_: _description - index
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
