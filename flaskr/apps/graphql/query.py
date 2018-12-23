import graphene
from .utils import FIELDS_TO_RETRIEVE


def create_name(outer_model):
    return '{}s'.format(outer_model.__name__.lower())


def create_value(outer_type):
    return graphene.List(lambda: outer_type, id=graphene.Int())


def create_resolver_name(outer_name):
    return 'resolve_{}'.format(outer_name)


def create_resolver(outer_type, outer_model):

    def resolver(self, info, *args, **kwargs):
        query = outer_type.get_query(info)
        if kwargs:
            for key, val in kwargs.items():
                query = query.filter(getattr(outer_model, key) == val)
        return query
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
