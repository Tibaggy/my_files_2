class Fighter:
    def attack(self):
        print(f'{self.class_} attacks!')
class Barbarian(Fighter):
    def __init__(self, name):
        self.class_ = 'barbarian'
        self.name = name
class Mage(Fighter):
    def __init__(self, name):
        self.class_ = 'mage'
        self.name = name
barb_name = input('Your barbarian name: ')
mage_name = input('Your mage name: ')

barb = Barbarian(barb_name)
mage = Mage(mage_name)

game = True

while game:
    action = input('Mage or Barbarian ')
    if action.lower() == 'mage':
        mage.attack()
    elif action.lower() == 'barbarian':
        barb.attack()
    elif action.lower() == 'exit':
        game = False
    else:
        print('Try again')