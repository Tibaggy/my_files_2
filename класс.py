# class Foo():
#     pass
# print(type(Foo))
class Animal():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def sleep(self):
        print(f'{self.name} Zzz...')
    def eat(self):
        print(f'{self.name} Om nom nom...')
class Cat(Animal):
    def say(self):
        print(f'{self.name} Meow!!!')
class Dog(Animal):
    def say(self):
        print(f'{self.name} Bark!!!')
fluffy = Cat('Snowball', 'white')
fluffy.sleep()
fluffy.eat()
smokey = Cat('Smokey', 'grey')
smokey.sleep()
smokey.eat()
cooper = Dog('Cooper', 'black')
cooper.say()
fluffy.say()