from . import db
from .base import ComponentMixin


class Processor(ComponentMixin, db.Model):
    cores = db.Column(db.Integer, nullable=False)
    l1_cache = db.Column(db.Integer, nullable=False)
    l2_cache = db.Column(db.Integer, nullable=False)
    l3_cache = db.Column(db.Integer, nullable=False)
