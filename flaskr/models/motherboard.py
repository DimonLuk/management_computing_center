from . import db
from .base import ComponentMixin


class Motherboard(db.Model, ComponentMixin):
    form_factor = db.Column(db.String(10), nullable=False)
    chipset = db.Column(db.String(10), nullable=False)
    pci_slots = db.Column(db.Integer, nullable=False, default=0)
    used_pci_slots = db.Column(db.Integer, nullable=False, default=0)
    ram_slots = db.Column(db.Integer, nullable=False, default=0)
    used_ram_slots = db.Column(db.Integer, nullable=False, default=0)

    @property
    def free_pci_slots(self):
        return self.pci_slots - self.used_pci_slots

    @property
    def free_ram_slots(self):
        return self.ram_slots - self.used_ram_slots
