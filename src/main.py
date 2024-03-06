
import pprint
from utils import getting_list_operation

import json
with open('../operations.json', 'r') as file:
    operations_list = json.load(file)

object_list = getting_list_operation(operations_list)


