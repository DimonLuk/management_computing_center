from . import db
from .base import ComponentMixin


class Motherboard(db.Model, ComponentMixin):
    form_factor = db.Column(db.String(10), nullable=False)
    chipset = db.Column(db.String(10), nullable=False)
