def mul(a, b):
    d = 0
    while b != 0:
        d += a
        b -= 1
    return d
print(mul(5, 5))