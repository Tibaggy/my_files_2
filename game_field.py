from random import uniform
import pickle
def saves(f):
    with open('save.dat', 'wb') as sf:
        pickle.dump(f,sf)
    print('Game saved!')
def loading():
    with open('save.dat', 'rb') as lf:
        loaded = pickle.load(lf)
    print('Game loaded!')
    return loaded
percent = 40
def build(x):
    v = []
    f = []
    for i in range(x):
        v.append('_')
    for i in range(x):
        f.append(v[:])
    return f

def user_f():
    return int(input("Укажите размер поля: "))
def user():
    return input('Выберите: DOWN, UP, LEFT, RIGHT или EXIT или LOAD или SAVE: ')

def start(x):
    x[0][0] = 'x'
    return x
def show_field(f):
    for i in f:
        print(' '.join(i))
def centre():
    game = True
    fields = user_f()
    field = start(build(fields))
    obstacles(field, percent)
    show_field(field)

    while game:
        user_d = user()
        if user_d == 'save':
            saves(field)
        elif user_d == 'load':
            field = loading()
        position = find_position(field)
        field = direction(user_d, field, position)
        if user_d == 'exit':
            game = False
        if game:
            show_field(field)
def block(d):
    print(f'Oops... Move to {d} is blocked!')

def check_obs(d, f, p):
    x, y = p
    flag = False
    if d == 'up':
        if f[x - 1][y] == '#':
            flag = True
    elif d == 'right':
        if  y + 1 > len(f) - 1:
            if f[x][0] == '#':
                flag = True
        else:
            if f[x][y + 1] == '#':
                flag = True
    elif d == 'down':
        if x + 1 > len(f) - 1:
            if f[0][y] == '#':
                flag = True
        else:
            if f[x + 1][y] == '#':
                flag = True
    elif d == 'left':
        if f[x][y - 1] == '#':
            flag = True
    return flag
 
def up(f, p):
    x, y = p
    f[x - 1][y] = 'x'
    f[x][y] = '_'
    return f
def down(f, p):
    x, y = p
    if x + 1 > len(f) - 1:
        f[0][y] = 'x'
        f[x][y] = '_'
    else:
        f[x + 1][y] = 'x'
        f[x][y] = '_'
    return f
def left(f, p):
    x, y = p
    f[x][y - 1] = 'x'
    f[x][y] = '_'    
    return f
def right(f, p):
    x, y = p
    if y + 1 > len(f) - 1:
        f[x][0] = 'x'
        f[x][y] = '_'
    else:
        f[x][y + 1] = 'x'
        f[x][y] = '_'
    return f
def direction(d, f, p):
    obs = check_obs(d, f, p)
    if d.lower() == "up" and not obs:
        field = up(f, p)
    elif d.lower() == 'down' and not obs:
        field = down(f, p)
    elif d.lower() == "right" and not obs:
        field = right(f, p)
    elif d.lower() == 'left' and not obs:
        field = left(f, p)
    else:
        block(d)
    return field
def find_position(f):
    x_pos = 0
    y_pos = 0
    f_lenght = range(len(f))
    for x in f_lenght:
        for y in f_lenght:
            if f[x][y] == 'x':
                x_pos = x
                y_pos = y
                break
    return x_pos, y_pos
def obstacles(f, o):
    f_lenght = range(len(f))
    obs_percent = o / 100
    for i in f_lenght:
        for n in f_lenght:
            if uniform(0, 1) <= obs_percent and f[i][n] != 'x':
                f[i][n] = '#'
    return f
centre()