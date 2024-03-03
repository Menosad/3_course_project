class Operation():
    def __init__(self, date, descrpt, agent, unick, amount, state, accaunt):
        self.date = date
        self.descrpt = descrpt
        self.agent = agent
        self.id = unick
        self.amount = amount
        self.state = state
        self.account = accaunt

    def get_date(self):
        from datetime import datetime
        thedate = datetime.fromisoformat(self.date)
        return datetime.strftime(thedate, '%d.%m.%Y')



# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.