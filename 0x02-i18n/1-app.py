#!/usr/bin/env python3
'''
Setting up a basic Flask app
'''
from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


class Config:
    '''
    This class configures available languages, default local e and timezone
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route("/")
def index():
    '''This function renders an HTML template'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
