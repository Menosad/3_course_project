class Operation():
    def __init__(self, date, descrpt, agent, unick, amount, state, accaunt):
        self.date = date
        self.descrpt = descrpt
        self.agent = agent
        self.id = unick
        self.amount = amount
        self.state = state
        self.account = accaunt
        self.unick = unick

    def f_date(self):
        from datetime import datetime
        thedate = datetime.fromisoformat(self.date)
        return datetime.strftime(thedate, '%d.%m.%Y')

    def f_agent(self):
        #"from": "7000 79** **** 6361",
        lst = self.agent.split()
        list_num = list(lst[-1])
        new_lst = list_num[0:2]
        for i in range(2, len(list_num)):
            if i % 4 == 0:
                new_lst.append(' ')
                new_lst.append(list_num[i])
            else:
                new_lst.append(list_num[i])
        new_num = ''
        for j in range(len(new_lst)):
            if j in (7, 8) or j in (10, 11, 12, 13):
                new_num += '*'
            else:
                new_num += new_lst[j]

        return ' '.join(lst[:-1]) + ' ' + new_num

    def check(self):
        lst = self.account.split()
        check = lst[-1]
        word = ' '.join(lst[:-1])
        return word + ' ' + check[-4:].rjust(6, '*')

    def money(self):
        suma = self.amount['amount']
        unit = self.amount['currency']['name']
        return suma + ' ' + unit
        pass
