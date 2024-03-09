import pytest

from src import utils
import os

coll = [
    {"date": "2019-08-26T10:50:58.294041", "state": "EXECUTED"},
    {"date": "2019-07-03T18:35:29.512364", "state": "CANCELED"},
    {}
]

col = {"date": "2019-08-26T10:50:58.294041", "state": "EXECUTED"}

PATH = os.path.join('test_json_file.json')


def test_get_file():
    assert utils.get_file(PATH) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                     'operationAmount': {'amount': '31957.58',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                     'to': 'Счет 64686473678894779589'}]


def test_get_operation_list():
    assert utils.get_operation_list(coll) == [{"date": "2019-08-26T10:50:58.294041", "state": "EXECUTED", }]


def test_get_date():
    assert utils.get_date(col) == '26.08.2019'
