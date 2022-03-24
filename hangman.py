from random import choice
def game():
    progress = True
    word = ['orange', 'banana', 'apple', 'milk']
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)
        if not check_mistake(word_in_play, user_guess):
            lifes = check_attempt(lifes)

        if lifes == 0:
            lose_speech()
            break

        if not progress:
            win_speech()
            break
def build_template(t, w, g=''):
    for i in range(len(w)):
        if w[i] == g:
            t[i] = g
    return t


def start_template(w):
    t = []
    for l in w:
        t.append('_')
    return t
def get_word(w):
    w = choice(w)
    return w
    
def list_to_string_convert(t):
    t = "".join(t)
    return t

def welcome_speech(t):
    print(f"Добро пожаловать в игру - hangman 2000 \nВаша задача угадать слово за несколько попыток, \nИначе вас ждёт расплата! \nЗагаданное слово состоит из {len(t)} букв {t}")

def user_input():
    s = input('Введите букву:')
    return s
def print_result(g):
    print(f'Результат: {g}')
def check_win(g):
    for i in g:
        if i == "_":
            return True
    return False
def check_mistake(w, g):
    for i in w:
        if i == g:
            return True
    return False
def check_attempt(life):
    life -= 1
    print(f'Минус одна жизнь.\nОсталось {life} попытки')
    return life
def win_speech():
    print('Победа!')
def lose_speech():
    print('Проигрыш')
game()