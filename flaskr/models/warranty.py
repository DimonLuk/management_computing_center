from sqlalchemy.orm import relationship
from . import db
from .base import DefaultMixin


class Warranty(db.Model, DefaultMixin):
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    components = relationship('ComponentMetaInfo', back_populates='warranty')

    def __repr__(self):
        return '<Warranty object id="{}" from="{}" to="{}">'.format(
            self.id, self.start_date, self.end_date
        )
