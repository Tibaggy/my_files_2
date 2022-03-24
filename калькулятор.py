def main ():
    progress = True
    while progress != False:
        user_input_1 = user()
        if str(user_input_1).lower() != 'выход':
            user_input_2 = user2()
            user_znak = user3()
            end = calc(user_input_1, user_input_2, user_znak)
            print(end)
        else:
            print('Вы вышли\nПрограмма закрывается...')
            progress = False

def user():
    return input('Введите первое число или же можете написать "выход" для выхода: ')

def user2():
    return int(input('Введите второе число: '))

def user3():
    return input('Выберите знак ( /, *, +, -, %): ')

def calc(x, y, z):
    if z == '/':
        return int(x) / y
    elif z == '-':
        return int(x) - y
    elif z == '+':
        return int(x) + y
    elif z == '*':
        return int(x) * y
    elif z == '%':
        return int(x) % y
main()