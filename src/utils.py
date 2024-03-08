import pprint
from clases import Operation


def getting_list_operation(array: list):
    list_ = []
    for dic in array:
        if 'date' not in dic:
            pass
        elif 'from' not in dic.keys():
            date = dic['date']
            unick = dic['id']
            state = dic['state']
            amount = dic['operationAmount']
            descrpt = dic['description']
            agent = None
            accaunt = dic['to']
            oper_n = Operation(date, descrpt, agent, unick, amount, state, accaunt)
            list_.append(oper_n)
        else:
            date = dic['date']
            unick = dic['id']
            state = dic['state']
            amount = dic['operationAmount']
            descrpt = dic['description']
            agent = dic['from']
            accaunt = dic['to']
            oper_n = Operation(date, descrpt, agent, unick, amount, state, accaunt)
            list_.append(oper_n)

    return list_


def interval_selection(lst: list):
    interval = []
    for object in lst:
        if object.state == 'EXECUTED':
            interval.append(object)
    return interval


def conclusion(lst: list):
    for operation in lst[:10]:
        if operation.agent == None:
            print(f"{operation.f_date()} {operation.descrpt}\n"
                  f"{operation.check()}\n"
                  f"{operation.money()}")
        else:
            print(f"{operation.f_date()} {operation.descrpt}\n"
                  f"{operation.f_agent()} -> {operation.check()}\n"
                  f"{operation.money()}")
