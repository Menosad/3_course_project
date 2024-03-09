import json

def get_file(pth):
    with open(pth, encoding='utf-8') as file:
        lst = json.load(file)
    return lst


def get_operation_list(dic: list):
    dic_filtred = list(filter(lambda x: x.get('date'), dic))
    filtred_list = list(filter(lambda e: e['state'] == 'EXECUTED', dic_filtred))
    lst = sorted(filtred_list, key=lambda d: d['date'], reverse=True)
    return lst

def get_date(col: dict):
    s = col['date']
    ind = s.find('T')
    lst = s[:ind].split('-')
    return lst[-1] + '.' + lst[-2] + '.' + lst[-3]
