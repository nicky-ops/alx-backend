#!/usr/bin/env python3
'''
Setting up a basic Flask app
'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    '''
    This class configures available languages, default local e and timezone
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home():
    '''This function renders an HTML template'''
    return render_template('3-index.html')

@babel.localeselector
def get_locale():
    '''
    This function gets a locale from request
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
