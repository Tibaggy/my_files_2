names = ['Firewey', 'Dewedor', 'Silverde', 'StupidNames']
classes = ['amazon', 'necromancer', 'paladin', 'druid']
levels = [2, 2, 3, 4]
def get_stats(name, name_list, class_list, level_list):
    t = name_list.index(name)
    char_class = class_list[t]
    char_level = level_list[t]
    return char_class, char_level
player_3 = get_stats('Silverde', names, classes, levels)
print(player_3)