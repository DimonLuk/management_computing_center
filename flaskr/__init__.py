import os
from .apps._agregator import bp as _agregator
from .apps.health_check import bp as health_check
from .apps.graphql.graphql import bp as graphql
from flask import Flask
from .models import db, migrate


def create_app(test_mode=False, dev_mode=True, prod_mode=False):
    app = Flask(__name__, instance_relative_config=True)
    connection = 'sqlite:///models/dev_db.sql'
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=connection,
        SQLALCHEMY_DATABASE_URI=connection
    )
    if prod_mode:
        app.config.from_pyfile('prod_conf.py')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(health_check)
    app.register_blueprint(graphql)
    if dev_mode:
        app.register_blueprint(_agregator)

    @app.route('/basic_health_check')
    def basic_health_check():
        return 'Server is started!'

    return app
