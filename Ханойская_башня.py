def show_move(fr, to):
    print(f'Move from {fr} to {to}')
def hanoi(n, fr, to, spare):
    if n == 1:
        show_move(fr, to)
    else:
        hanoi(n - 1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(n - 1, spare, to, fr)
hanoi(3, 'p1', 'p2', 'p3')