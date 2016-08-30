from collections import OrderedDict
import json

od = OrderedDict()
od['b'] = 1
od['a'] = 2
od['cat'] = 3
od['giraffe'] = 4

print(od)

print(json.dumps(od))
