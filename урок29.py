# class Foo:
#     def __init__(self, number):
#         self.number = number
#     def __str__(self):
#         return f'Foo: {self.number}'
    
#     def __add__(self, other):
#         result = self.number + other.number
#         return Foo(result)

#     def __sub__(self, other):
#         result = self.number - other.number
#         return Foo(result)

class Foo(int):
    def __init__(self, number):
        self.number = number
# a = Foo(2)
# b = Foo(1)

# c = a + b
# print(c)
a = Foo(3)
print(a.number)
a.number = 4
print(a.number)
a.new_data = 'Hello world'
print(a.new_data)