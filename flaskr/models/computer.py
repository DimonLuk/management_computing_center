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
    motherboard = relationship('motherboard', backref='computer')

    ram_id = db.Column(db.Integer, db.ForeignKey('ram.id',
                                                 ondelete='CASCADE'))
    ram = relationship('ram_id', backref='computer')

    processor = db.Column(db.Integer, db.ForeignKey('processor.id',
                                                    ondelete='CASCADE'))
    processor = relationship('processor', backref='computer')

    def __repr__(self):
        return '<Computer computer id="{}" room="{}">'.format(
            self.id, self.room
        )
