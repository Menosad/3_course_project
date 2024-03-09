import json
import os



PATH = os.path.join('..', 'operations.json')


def get_operation_list():
    with open(PATH, encoding='utf-8') as file:
        lst = json.load(file)
        filt = list(filter(lambda x: x.get('date'), lst))
        filtred_list = list(filter(lambda s: s['state'] == 'EXECUTED', filt))
        final = sorted(filtred_list, key=lambda d: d['date'], reverse=True)
    return final



