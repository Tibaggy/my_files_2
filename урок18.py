def add_one(x):
    return x + 1
def square(x):
    return x * x
def apply_functions(l, x):
    for f in l:
        print(f(x))
apply_functions([add_one, square, float], 4)