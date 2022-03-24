def add_one(x):
    return x + 1
map_object = map(add_one, [1, 2, 3, 4])
for  el in map_object:
    print(el)