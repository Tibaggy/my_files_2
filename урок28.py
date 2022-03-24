class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Cat: {self.name}'

fluffy = Cat('fluffy')

print(fluffy)