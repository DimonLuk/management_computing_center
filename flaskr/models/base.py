from . import db, get_db_session
from sqlalchemy.ext.declarative import declared_attr
from importlib import import_module


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

    @property
    def info(self):
        ComponentMetaInfo = import_module('flaskr.models.component_meta_info')\
            .ComponentMetaInfo
        with get_db_session() as session:
            return session.query(ComponentMetaInfo)\
                .get(self.component_meta_info_id)

    @property
    def type(self):
        return type(self).__name__

    def __repr__(self):
        return '<{} object>'.format(self.type)
