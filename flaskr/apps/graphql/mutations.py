import graphene
from flaskr.models import get_db_session
from .utils import FIELDS_TO_RETRIEVE


def make_create_input_cls(name, attribute):
    return type(name, (graphene.InputObjectType, attribute), {})


def make_create_cls(name, model, typ, attribute, create_input_cls,
                    general_name):
    result_cls = None

    def general_mutate(self, info, input):
        result = None
        with get_db_session() as session:
            result = model(**input)
            session.add(result)
        return result_cls(**{'{}'.format(general_name): result})
    arguments = type('Arguments', tuple(), {
        'input': create_input_cls(required=True)
    })
    result_cls = type(name, (graphene.Mutation,), {
        '{}'.format(general_name): graphene.Field(lambda: typ),
        'Arguments': arguments,
        'mutate': general_mutate
    })
    return result_cls


def make_update_input_cls(name, attribute):
    return type(name, (graphene.InputObjectType, attribute), {
        'id': graphene.Int()
    })


def make_update_cls(name, model, typ, attribute, update_input_cls,
                    general_name):
    result_cls = None

    def general_mutate(self, info, input):
        result = None
        with get_db_session() as session:
            result = session.query(model).get(input.get('id'))
            for key, value in input.items():
                if key != 'id':
                    setattr(result, key, value)
        return result_cls(**{'{}'.format(general_name): result})
    arguments = type('Arguments', tuple(), {
        'input': update_input_cls(required=True)
    })
    result_cls = type(name, (graphene.Mutation,), {
        '{}'.format(general_name): graphene.Field(lambda: typ),
        'Arguments': arguments,
        'mutate': general_mutate
    })
    return result_cls


def make_delete_input_cls(name, attribute):
    return type(name, (graphene.InputObjectType, attribute), {
        'id': graphene.Int()
    })


def make_delete_cls(name, model, typ, attribute, delete_input_cls,
                    general_name):
    result_cls = None

    def general_mutate(self, info, input):
        with get_db_session() as session:
            result = session.query(model).get(input.get('id'))
            session.query(model).filter(model.id == input.get('id')).delete()
        return result_cls(**{'{}'.format(general_name): result})
    arguments = type('Arguments', tuple(), {
        'input': delete_input_cls(required=True)
    })
    result_cls = type(name, (graphene.Mutation,), {
        '{}'.format(general_name): graphene.Field(lambda: typ),
        'Arguments': arguments,
        'mutate': general_mutate
    })
    return result_cls


class MetaMutation(type(graphene.ObjectType)):
    def __new__(cls, name, bases, dict_):
        for obj in FIELDS_TO_RETRIEVE:
            model = obj.get('model')
            typ = obj.get('type')
            attribute = obj.get('attribute')

            name = model.__name__.lower()

            # CreateModelInput
            create_input_name = 'Create{}Input'.format(model.__name__)
            create_input_cls = make_create_input_cls(create_input_name,
                                                     attribute)

            # CreateModel
            create_name = 'Create{}'.format(model.__name__)
            create_cls = make_create_cls(create_name, model, typ, attribute,
                                         create_input_cls, name)

            # UpdateModelInput
            update_input_name = 'Update{}Input'.format(model.__name__)
            update_input_cls = make_update_input_cls(update_input_name,
                                                     attribute)

            # UpdateModel
            update_name = 'Update{}'.format(model.__name__)
            update_cls = make_update_cls(update_name, model, typ, attribute,
                                         update_input_cls, name)

            # DeleteModelInput
            delete_input_name = 'Delete{}Input'.format(model.__name__)
            delete_input_cls = make_delete_input_cls(delete_input_name,
                                                     attribute)

            # DeleteModel
            delete_name = 'Delete{}'.format(model.__name__)
            delete_cls = make_delete_cls(delete_name, model, typ, attribute,
                                         delete_input_cls, name)

            self_create_name = 'create_{}'.format(name)
            self_update_name = 'update_{}'.format(name)
            self_delete_name = 'delete_{}'.format(name)
            dict_[self_create_name] = create_cls.Field()
            dict_[self_update_name] = update_cls.Field()
            dict_[self_delete_name] = delete_cls.Field()
        return super(MetaMutation, cls).__new__(cls, name, bases, dict_)


class Mutation(graphene.ObjectType, metaclass=MetaMutation):
    pass
