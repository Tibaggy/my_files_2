from random import randint
class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
    def __str__(self):
        return f'This potion named: {self.name}, {self.quality}'
    def get_quality(self):
        return self.quality
    def get_name(self):
        return self.name
    def __add__(self, other):
        i = int(len(self.name) / 2)
        n = int(len(other.name) / 2)
        new_name = self.name[:i] + other.name[:n]
        new_quality = (self.quality + other.quality) / 2
        return Potion(new_name, new_quality)
    def __sub__(self, other):
        new_quality = other.quality - randint(1, 100)
        return Potion(self.name, new_quality)
    def check_quality(self):
        if self.quality > 75:
            print('Potion is very good')
        elif self.quality > 50:
            print('Potion is average')
        else:
            print('Potion has bad quality')
    def __mul__(self):
        new_quality = self.quality * 2
        return Potion(self.name, new_quality)
class QualityPotion(Potion):
    def special(self):
        return QualityPotion(self.name, self.quality + 20) 
class NotQualityPotion(Potion):
    def special(self):
        return QualityPotion(self.name, self.quality - 20) 
# quality = randint(1, 100)
# qPotion = QualityPotion('Veritaseum', quality)
# print(qPotion)
# print(qPotion.get_quality())
# updgardePotion = qPotion.special()
# print(updgardePotion.get_quality())
game = True
potions = {}
while game:
    potion = input(f'q - for quality or n - for non quality ').lower()
    if potion == 'exit':
        game = False
    else:
        potion_name = input('Enter potion name: ')
        potion_quality = randint(1, 100)
        if potion == 'q':
            new_potion = QualityPotion(potion_name, potion_quality)
        else:
            new_potion = NotQualityPotion(potion_name, potion_quality)
        potions[potion_name] = new_potion

    if len(potions) >= 2:
        sub_or_add = input('(-) or (+) ')
        potion_one = potions.popitem()[1]
        potion_two = potions.popitem()[1]
        if sub_or_add == '+':
            mix = potion_one + potion_two
        else:
            mix = potion_one - potion_two
        print('Start mixen...')
        if mix.get_quality() < 30:
            print('Kaboom!!! You die...')
            game = False
        else:
            potions[mix.get_name()] = mix
            print(f'Your potions: {potions.keys()}')
            print(f'Potion quality: {mix.get_quality}, be careful next time!')