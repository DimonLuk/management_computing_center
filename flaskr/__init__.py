import os
from flask import Flask
from .apps import health_check
from .apps.graphql import graphql


def create_app(test_mode=False, dev_mode=True, prod_mode=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='sqlite:///flaskr/models/dev_db.sql'
    )
    if prod_mode:
        app.config.from_pyfile('prod_conf.py')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(health_check.bp)
    app.register_blueprint(graphql.bp)

    @app.route('/basic_health_check')
    def basic_health_check():
        return 'Server is started!'

    return app
