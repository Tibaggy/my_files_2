word = input('')
a = 0
p = 0
glasn = 'ёеаоэяиюыу'
soglasn = 'йцкнгшщзхфвпрлджчсмтб'
for i in word:
    for s in glasn:
        if i == s:
            a += 1
    for g in soglasn:
        if i == g:
            p += 1
print(f'Гласных букв: {a}. Согласных букв: {p}')
