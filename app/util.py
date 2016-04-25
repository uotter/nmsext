import json, datetime
from sqlalchemy.ext.declarative import DeclarativeMeta


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def obj_to_json(obj_list):
    out = [q.__dict__ for q in obj_list]
    for objs, instance in zip(out, obj_list):
        for obj in objs.values():
            if callable(obj):
                for name in obj.mapper.relationships.keys():
                    tmp = getattr(instance, name).__dict__
                    if "_sa_instance_state" in tmp.keys():
                        tmp.pop("_sa_instance_state")
                        tmp.pop("id")
                        objs.update(tmp)
                    objs.pop(name)
        if "_sa_instance_state" in objs.keys():
            objs.pop("_sa_instance_state")
    return out


def query_result_json(query_result):
    """
    Convert query result to json format
    """
    if isinstance(query_result, list):
        mid_result = obj_to_json(query_result)
        result = {'data': mid_result}
    elif getattr(query_result, '__dict__', ''):
        mid_result = obj_to_json([query_result])
        result = {'data': mid_result}
    else:
        result = {'data': query_result}
    return json.dumps(result, cls=ComplexEncoder)

# another implementation of jsonencoder, but not tested
# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     json.dumps(data)     # this will fail on non-encodable values, like other classes
#                     fields[field] = data
#                 except TypeError:
#                     if isinstance(data, datetime.datetime):
#                         fields[field] = data.isoformat()
#                     elif isinstance(data, datetime.date):
#                         fields[field] = data.isoformat()
#                     elif isinstance(data, datetime.timedelta):
#                         fields[field] = (datetime.datetime.min + data).time().isoformat()
#                     else:
#                         fields[field] = None
#             # a json-encodable dict
#             return fields
#         return json.JSONEncoder.default(self, obj)