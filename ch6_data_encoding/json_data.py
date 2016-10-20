import json
from pprint import pprint
from collections import OrderedDict

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# turn python to json
json_string = json.dumps(data)
print(json_string)

# turn string to python
loaded_json = json.loads(json_string)
print(loaded_json)

# can also be used to dump to and read from files
with open('data_files/data.json', 'w') as f:
    json.dump(data, f)

# pprint can be useful for more readable output when reading json
pprint(loaded_json)
print()

# can turn JSON into different kinds of python data structures if desired
# here we turn it into OrderedDict instead of normal dict
data_ordered_dict = json.loads(json_string, object_pairs_hook=OrderedDict)
print(data_ordered_dict)
print()


# here we turn it into a python object
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data_obj = json.loads(json_string, object_hook=JSONObject)
print(data_obj)
print(data_obj.name)
print()

# can use indent argument to prettify JSON serialization as well, similar to pprint
print(json.dumps(data, indent=4))

# can designate sorting keys as well
print(json.dumps(data, sort_keys=True))


# instances are generally not serializable as JSON, must supply a function that takes an instance and returns a dict
# that can be serialized
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
try:
    print(json.dumps(p))
except TypeError:
    print('Type Error')


def serialize_instance(obj):
    d = { '__classname__': type(obj).__name__ }
    d.update(vars(obj))
    return d


# and going the other way
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
