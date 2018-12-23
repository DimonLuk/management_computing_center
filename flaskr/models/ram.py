from . import db
from .base import ComponentMixin


class Ram(ComponentMixin, db.Model):
    capacity = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
