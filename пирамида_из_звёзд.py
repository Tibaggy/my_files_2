user = int(input('Введите число этажей: '))
def centre():
    if user % 2  == 0:
        print('Введите нечётное число')
    else:
        pyramid(user)
def pyramid(x):
    for i in range(x // 2):
        print('*' * (i + 1))

    for i in range((x // 2) + 1, 0, -1):
        print('*' * (i))
centre()