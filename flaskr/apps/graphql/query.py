import graphene
from .utils import FIELDS_TO_RETRIEVE
from sqlalchemy import and_
from flaskr.models.component_meta_info import ComponentMetaInfo
from flaskr.models import get_db_session


def create_name(outer_model):
    return '{}s'.format(outer_model.__name__.lower())


def create_value(outer_type):
    return graphene.List(lambda: outer_type, id=graphene.Int(),
                         last=graphene.Boolean(),
                         status=graphene.String())


def create_resolver_name(outer_name):
    return 'resolve_{}'.format(outer_name)


def create_resolver(outer_type, outer_model):

    def resolver(self, info, *args, **kwargs):
        with get_db_session() as session:
            query = session.query(outer_model)
            skip_fields = ('last',)
            special_filters = ('status',)
            if kwargs:
                if kwargs.get('last'):
                    query = query.order_by(outer_model.id.desc()).first()
                    return [query]
                for key, val in kwargs.items():
                    if key == 'status':
                        if getattr(outer_model, 'component_meta_info', None):
                            query = query.join(
                                ComponentMetaInfo,
                                and_(
                                    outer_model.component_meta_info_id ==
                                    ComponentMetaInfo.id,
                                    ComponentMetaInfo.status == val
                                )
                            )
                    if key not in skip_fields and \
                            key not in special_filters and \
                            getattr(outer_model, key, None):
                        query = query.filter(getattr(outer_model, key) == val)
            return query.all()
    return resolver


class MetaQuery(type(graphene.ObjectType)):
    def __new__(cls, name, bases, dict_):
        for obj in FIELDS_TO_RETRIEVE:
            typ = obj.get('type')
            model = obj.get('model')

            name = create_name(model)
            dict_[name] = create_value(typ)

            resolver_name = create_resolver_name(name)
            dict_[resolver_name] = create_resolver(typ, model)
        return super(MetaQuery, cls).__new__(cls, name, bases, dict_)


class Query(graphene.ObjectType, metaclass=MetaQuery):
    pass
