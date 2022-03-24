# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fib(n - 1) + fib (n - 2)
# print(fib(35))
# def fib(n):
#     r = [1, 1]
#     for i in range(2, n):
#         next_num = r[i -1] + r[i -2]
#         r.append(next_num)
#     return r[-1]
# print(fib(7))
def fib_memoize(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_memoize(n - 1, d) + fib_memoize(n - 2, d)
        d[n] = ans
        return ans
base_case = {0: 1, 1: 1}
print(fib_memoize(35, base_case))