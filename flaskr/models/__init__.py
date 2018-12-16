from flask import g, current_app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


def get_engine():
    if 'engine' not in g:
        engine = create_engine(current_app.config['DATABASE'])
        g.engine = engine

    return g.engine


def dispose_engine():
    engine = g.pop('engine', None)
    if engine:
        engine.dispose()


@contextmanager
def get_db_session():
    Session = sessionmaker()
    Session.configure(bind=get_engine())
    db_session = Session()
    db_session = db_session

    yield db_session

    db_session.close()


Base = declarative_base()
