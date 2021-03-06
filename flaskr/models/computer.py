from sqlalchemy.orm import relationship
from . import db
from .base import DefaultMixin


class Computer(db.Model, DefaultMixin):
    room = db.Column(db.String(10), nullable=False)

    trunk_id = db.Column(db.Integer, db.ForeignKey('trunk.id',
                                                   ondelete='CASCADE'))
    trunk = relationship('Trunk', backref='computer')

    motherboard_id = db.Column(db.Integer, db.ForeignKey('motherboard.id',
                                                         ondelete='CASCADE'))
    motherboard = relationship('Motherboard', backref='computer')

    ram_id = db.Column(db.Integer, db.ForeignKey('ram.id',
                                                 ondelete='CASCADE'))
    ram = relationship('Ram', backref='computer')

    processor_id = db.Column(db.Integer, db.ForeignKey('processor.id',
                                                       ondelete='CASCADE'))
    processor = relationship('Processor', backref='computer')

    def __repr__(self):
        return '<Computer computer id="{}" room="{}">'.format(
            self.id, self.room
        )
