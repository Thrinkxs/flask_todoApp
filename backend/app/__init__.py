from flask import Flask
import psycopg2
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='../../frontend/templates',
                static_folder='../../frontend/static')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkavnntb:Lvxr4i1weHxWW5wMRyHoCoPyXPwkfL5J@rain.db.elephantsql.com/mkavnntb'
    database_url = 'postgresql://mkavnntb:Lvxr4i1weHxWW5wMRyHoCoPyXPwkfL5J@rain.db.elephantsql.com/mkavnntb'
    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)

    from routes import blueprint
    app.register_blueprint(blueprint)

    return app
