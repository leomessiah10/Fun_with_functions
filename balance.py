print('This program helps in calculating the interests of the amounts')

amount = [1000, 10000, 5000, 7070]
rate = 0.5
count = len(amount)

def add_interest(balances, rates):
    for i in range(count):
        balances[i] = balances[i] *(1+ rates)
        amount[i] = balances[i]

def test():
    add_interest(amount, rate)
    print(amount)

test()
