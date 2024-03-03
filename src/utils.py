import pprint
from clases import Operation



def getting_list_operation(array: list):
    list_ = []
    for dic in array:
        if 'date' not in dic.keys():
            pass
        elif 'from' not in dic.keys():
            date = dic['date']
            unick = dic['id']
            state = dic['state']
            amount = dic['operationAmount']
            descrpt = dic['description']
            agent = None
            accaunt = dic['to']
            oper_n = Operation(date, unick, state,
                               amount, descrpt, agent, accaunt)
            list_.append(oper_n)
        else:
            date = dic['date']
            unick = dic['id']
            state = dic['state']
            amount = dic['operationAmount']
            descrpt = dic['description']
            agent = dic['from']
            accaunt = dic['to']
            oper_n = Operation(date, unick, state,
                               amount, descrpt, agent, accaunt)
            list_.append(oper_n)

    return list_
