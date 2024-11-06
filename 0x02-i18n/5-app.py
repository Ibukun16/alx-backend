#!/usr/bin/env python3
"""A basic flask app that mimick
creating a user login system
"""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Flask babel configuration

    Return:
            _type_: _description_
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


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
    """Get a user based on the user id

    Return:
            _type_: _description_(the user id)
    """
    login_id = request.args.get('logn_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Perform some routine tasks before
    the resolution of each request
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
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    """Use index to retrive index as homepage

    Return:
            _type_: _description - index
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
