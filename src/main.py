from utils import getting_list_operation, interval_selection, conclusion

import json
with open('../operations.json', 'r') as file:
    operations_list = json.load(file)

object_list = getting_list_operation(operations_list)

object_list.sort(key=lambda obj: obj.date, reverse=True)

interval = interval_selection(object_list)

conclusion(interval)
