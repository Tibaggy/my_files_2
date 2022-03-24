classes = ['pirate', 'mage', 'druid']
items = ['sword', 'staff', 'pistol', 'shield']
potion = ['health', 'mana']
name = input('name: ')
class_user = input(f'class: {classes} ')
if class_user not in classes:
    class_user = input(f'wrong class: {classes} ')
item_user = input(f'item: {items} ')
if item_user not in items:
    item_user = input(f'wrong item: {item} ')
potion_user =  input(f'potion: {potion} ')
if potion_user not in potion:
    potion_user =  input(f'wrong potion: {potion} ')

character = {name: {class_user: {'items': item_user, 'potion': potion_user}}}
print(character)