#!/usr/bin/env python3
"""Create a basic Flash app"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config(object):
    """Flask Babel configuration

    Returns:
            _type_: _description_
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the locale from a webpage

    Return:
            _type_: _description_
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
        ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            print(query_table['locale'])
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Use render template to get the index page

    Return:
            _type_: _description_
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
