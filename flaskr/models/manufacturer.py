from sqlalchemy.orm import relationship
from . import db
from .base import DefaultMixin


class Manufacturer(db.Model, DefaultMixin):
    title = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    components = relationship('ComponentMetaInfo',
                              back_populates='manufacturer')
    phone_number = db.Column(db.String(13), nullable=True)

    def __repr__(self):
        return '<Manufacturer object id="{}" title="{}">'.format(
            self.title, self.address
        )
