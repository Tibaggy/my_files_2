def find_uniq(x):
    v = 0
    t = 0
    for i in x:
        if i % 2 == 0:
            v += 1
            uniq = i     
        else:
            t += 1
            uniq_2 = i
    if v > t:
        return uniq_2
    else:
        return uniq
print(find_uniq([2, 4, 0, 100, 4, 11, 36]))
print(find_uniq([3, 5, 73, 13, 9, 12, 37]))