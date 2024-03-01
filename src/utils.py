import os
import pprint
import json

#Распаковываем и переводим в список словарей файл с банковскими операциями
with open('../operations.json', 'r') as file:
    operations_list = json.load(file)


