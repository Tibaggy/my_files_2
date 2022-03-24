def build_house(my_dream, colors):
    house = False
    roof_color = colors[0]
    house_color = colors[1]
    door_color = colors[2]
    roof = my_dream[0]
    walls = my_dream[1]

    while not house:
        roof_status = build_roof(roof, roof_color)
        walls_status = build_walls(walls, house_color)
        door_status = build_door(door_color, door_color)
        if roof_status == True and walls_status == True and door_status == True:
            house = True
            print('Поздравляю вы построили дом мечты!')
    return house
def build_roof(r, rc):
    """
    input: r - data for build roof, rc - data for color
    return: bool
    """
    return True
def build_walls(r, wc):
    """
    input: r - data for build walls, wc - data for roof color
    return: bool
    """
    return True
def build_door(r,dc):
    """
    input: r - data for build door< dc - data for roof color
    return: bool
    """
    return True
idea = ('roof', 'walls')
colors = ('red', 'white', 'blue')
build_house(idea, colors)
