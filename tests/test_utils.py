from src.utils import sum_func
from src.clases import Operation

dict_coll = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 801684332,
        "state": "EXECUTED",
        "date": "2019-11-05T12:04:13.781725",
        "operationAmount": {
            "amount": "21344.35",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 77613226829885488381"
    }]
dic1 = dict_coll[0]
dic2 = dict_coll[1]
dic3 = dict_coll[2]

oper1 = Operation(dic1['date'], dic1['description'], dic1['from'],
                  dic1['id'], dic1['operationAmount'], dic1['state'],
                  dic1['to'])

oper2 = Operation(dic2['date'], dic2['description'], dic2['from'],
                  dic2['id'], dic2['operationAmount'], dic2['state'],
                  dic2['to'])

oper3 = Operation(dic3['date'], dic3['description'], None,
                  dic3['id'], dic3['operationAmount'], dic3['state'],
                  dic3['to'])


# def test_getting_list_operation():
#     assert getting_list_operation(dict_coll) == [oper1, oper2, oper3]
#
#
# def test_execut_selection():
#     assert execut_selection([oper1, oper2, oper3]) == [oper1, oper2]

def test_sum_func():
    assert sum_func(3, 4) == 7
