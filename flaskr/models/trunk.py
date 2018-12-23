from . import db
from .base import ComponentMixin


class Trunk(ComponentMixin, db.Model):
    width = db.Column(db.Numeric(precision=8), nullable=False)
    height = db.Column(db.Numeric(precision=8), nullable=False)
    form_factor = db.Column(db.String(10), nullable=False)
