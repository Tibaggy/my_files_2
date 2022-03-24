savings = int(input(''))
interest = int(input(''))
time = int(input(''))
def bank(s, i=2, t=1):
    if i > 5:
        print('Максимальный процент в нашем банке 5% годовых')
        return False
    savings = calculate_savings(s, i, t)
    return savings
def calculate_savings(s, i, t):
    for n in range(t):
        s += s * (i / 100)
    return s 
total_savings = bank(savings, interest, time)
if total_savings != False:
    print(f'Ваш итоговый вывод: {total_savings}')
