money = int(input('money: '))

dict_ = {'тысяча': 0, 'пятьсот': 0, 'сто': 0, 'пятьдесят': 0,'десять': 0, 'пять': 0, 'рубль': 0}
def calc_banq(m):
    while m != 0:
        if m >= 1000:
            v = m / 1000
            dict_['тысяча'] = int(v)
            m = m - 1000 * int(v)
        if m >= 500:
            v = m / 500
            dict_['пятьсот'] = int(v)
            m = m - 500 * int(v)
        if m >= 100:
            v = m / 100
            dict_['сто'] = int(v)
            m = m - 100 * int(v)
        if m >= 50:
            v = m / 50
            dict_['пятьсот'] = int(v)
            m = m - 50 * int(v)
        if m >= 10:
            v = m / 10
            dict_['десять'] = int(v)
            m = m - 10 * int(v)
        if m >= 5:
            v = m / 5
            dict_['пять'] = int(v)
            m = m - 5 * int(v)
        if m >= 1:
            dict_['рубль'] = int(v)
            m = m - 1 * int(v)
    return dict_
print(calc_banq(money))