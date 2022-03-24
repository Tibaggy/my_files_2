
def F(n):
    if n == 1:
        return n
    return F(n - 1)
print(F(10))