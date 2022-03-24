class Foo:
    tag = 0
    def __init__(self, number):
        self.number = number
        Foo.tag += 1

a = Foo(3)
b = Foo(2)
print(a.tag)
print(b.tag)