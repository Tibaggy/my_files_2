dict_1 = {'A': 1, 'B': 2}
dict_2 = {'A': 3}
def merge_dict(a, b):
    dict_3 = {}
    for i in a:
        for n in b:
            if i == n:
                dict_3[i] = [a[i], b[n]]
            else:
                dict_3[i] = a[i]
    return dict_3
print(merge_dict(dict_1, dict_2))