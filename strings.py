d = {
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "valore"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}

import json
# print d["maps"]
# print d["masks"]["id"]

#print json.dumps(d)
di = json.dumps(d)
# print di
print type(di)
dict_res = json.loads(di)
print type(dict_res)
print dict_res
