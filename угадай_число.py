from random import randint

from_1_to_100 = int(randint(1, 100))
file = open('результаты', 'w+', encoding='utf8')
user = int(input('Попробуй угадать число от 1 до 100 '))
file.write(f'Попробуй угадать число от 1 до 100 {user}\n')
game = True
while game != False:
    if user != from_1_to_100:
        if user > from_1_to_100:
            print(f'Ответ неверный, попробуй числа ниже {user}')
            file.write(f'Ответ неверный, попробуй числа ниже {user}\n')
            user = int(input('Попробуй угадать число от 1 до 100 '))
            file.write(f'Попробуй угадать число от 1 до 100 {user}\n')
        else:
            print(f'Ответ неверный, попробуй числа выше {user}')
            file.write(f'Ответ неверный, попробуй числа выше {user}\n')
            user = int(input('Попробуй угадать число от 1 до 100 '))
            file.write(f'Попробуй угадать число от 1 до 100 {user}\n')
    else:
        print('Вы угадали верно!')
        file.write('Вы угадали верно!')
        game = False
file.close()
