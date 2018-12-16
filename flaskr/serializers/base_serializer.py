from flaskr.models import get_db_session
import json
from copy import deepcopy
import datetime


class BaseSerializer:

    def __init__(self, dict_or_instance):
        if isinstance(dict_or_instance, dict):
            self.obj = dict_or_instance
            self.instance = self.Meta.model(**self.obj)
        else:
            self.instance = dict_or_instance
            self.obj = self._map_instance()

        self._default_type_to_string = (
            {
            'type': datetime.date,
            },)

    def _map_instance(self):
        obj = self.instance.__dict__
        keys_to_pop = []
        for key in obj:
            if key.startswith('_'):
                keys_to_pop.append(key)
            if self.Meta.fields and self.Meta.fields != '__all__':
                if key not in self.Meta.fields:
                    keys_to_pop.append(key)

        for key in keys_to_pop:
            obj.pop(key, None)
        return obj

    @property
    def json(self):
        copied_obj = deepcopy(self.obj)
        types_to_string = []
        if 'types_to_string' not in self.Meta.__dict__:
            types_to_string = self._default_type_to_string
        else:
            default_types = [str(x.get('type')) for x in self._default_type_to_string]
            user_types = [str(x.get('type')) for x in self.Meta.types_to_string]
            intersection = list(set(default_types) & set(user_types))
            types_to_string = self.Meta.types_to_string
            for i in self._default_type_to_string:
                if str(i.get('type')) not in intersection:
                    types_to_string.append(i)
        for key in copied_obj:
            value = copied_obj.get(key)
            for x in types_to_string:
                if isinstance(value, x.get('type')):
                    func = x.get('func')
                    if func:
                        copied_obj[key] = func(value)
                    else:
                        copied_obj[key] = str(value)

        return json.dumps(copied_obj)

    def save(self):
        with get_db_session() as session:
            session.add(self.instance)
            session.commit()

    def update(self, obj):
        for key, value in obj:
            self.instance.__dict__[key] = value
            self.obj = self._map_instance()
