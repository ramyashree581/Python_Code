import json
from pprint import pprint

with open('sample.json') as f:
    data = json.load(f)

pprint(data)