import os
import pprint
import json

with open('../operations.json', 'r') as file:
    operations_list = json.load(file)

for dict in operations_list:


pprint.pprint(operations_list)