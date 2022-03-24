def sqrt(x, eps):
    res = eps
    if x == 0:
        return 0
    else:
        while True:
            if res * res == x:
                return res
            else:
                res = res + eps
print(sqrt(9, 0.0001))
