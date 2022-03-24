def apply_to_each(l, f):
    for i in range(len(l)):
        l[i] = f(l[i])
def change_direction(x):
    if x > 0:
        x = -x
    else:
        x = x * (-1)
    return x
numbers = [2,-2, 14, 0, 9.14, -1,25]
apply_to_each(numbers, change_direction)
print(numbers)