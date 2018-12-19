from sqlalchemy.orm import relationship
from . import db
from .base import DefaultMixin


class ComponentMetaInfo(db.Model, DefaultMixin):
    serial_number = db.Column(db.String(10), nullable=False)

    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id',
                                                          ondelete='CASCADE'))
    manufacturer = relationship('Manufacturer', back_populates='components')

    warranty_id = db.Column(db.Integer, db.ForeignKey('warranty.id',
                                                      ondelete='CASCADE'))
    warranty = relationship('Warranty', back_populates='components')

    component = relationship('ComponentMixin',
                             back_populates='component_meta_info')

    def __repr__(self):
        return '<ComponentMetaInfo object serial_number="{}">'.format(
            self.serial_number
        )
