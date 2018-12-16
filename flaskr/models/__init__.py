from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate() # NOQA


@contextmanager
def get_db_session():
    yield db.session
    db.session.commit()
