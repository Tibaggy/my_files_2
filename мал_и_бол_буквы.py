text = 'Fair is foul, and foul is fair: Hover through the fog and filthy air.'
big = 0
small = 0
alp_small = 'abcdefghijklmnopqrstuvwxyz'
alp_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in text:
    for s in alp_small:
        if i == s:
            small += 1
for i in text:
    for b in alp_big:
        if b == i:
            big += 1
print(f'Больших букв: {big}')
print(f'Маленьких букв: {small}')