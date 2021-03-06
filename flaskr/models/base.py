from . import db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
# from importlib import import_module


class DefaultMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True)


class ComponentMixin(DefaultMixin):
    @declared_attr
    def component_meta_info_id(cls):
        return db.Column(
            db.Integer,
            db.ForeignKey('componentmetainfo.id', ondelete='CASCADE')
        )

    @declared_attr
    def component_meta_info(cls):
        return relationship('ComponentMetaInfo', uselist=False,
                            backref='{}'.format(cls.__name__.lower()))

    def __repr__(self):
        return '<{} object>'.format(self.__tablename__)
