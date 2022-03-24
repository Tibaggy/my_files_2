# def avg(data):
#     assert not(len(data) == 0), "No data"
#     return sum(data) / len(data)
# foo = []
# print(avg(foo))


# def even(n):
#     if n % 2:
#         return False
#     else:
#         return True
# a = 3
# b = 4
# c = -1
# assert even(a) == False, "You code fails"
# assert even(b) == True, "You code fails"
# assert even(c) == False, "You code fails"
# print('Success!')


# try:
#     a = input('Enter: ')
#     b = input('Enter: ')
#     print(a * b)
#     print("Success")
# except:
#     print("Some bug")
# print("Always")


# while True:
#     try:
#         n = input('Enter: ')
#         n = int(n)
#         break
#     except ValueError:
#         print("Input int")
# print("Success")


# a = 11
# if a % 2 == 0:
#     raise ValueError(f'{a} - use odd numbers!')
# print("Success")


def is_palindrome(s):
    tmp = s
    tmp = tmp[::-1]
    if tmp == s:
        return True
    else:
        return 
        print('Yes')
def word(n):
    result = []
    for i in range(n):
        element = input('Enter element: ')
        result.append(element)
    if is_palindrome(result):
        print(f'{result} - is palindrome')
    else:
        print(f'{result} - not a palindrome')
word(2)