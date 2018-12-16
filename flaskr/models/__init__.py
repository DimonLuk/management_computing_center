from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate() # NOQA


@contextmanager
def get_db_session():
    Session = sessionmaker()
    Session.configure(bind=db)
    db_session = Session()
    db_session = db_session

    yield db_session

    db_session.close()
