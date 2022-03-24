date = ['Albert Einstein', 'Ada Lovelace', 'Guido van Rossum']
birthday = {'Albert Einstein': '14/03/1879', 'Ada Lovelace': '10/12/1815', 'Guido van Rossum': '31/01/1956'}

print('Welcome to the birthday dictionary. We know birdth dates of: ')
print(f'{date[0]}\n{date[1]}\n{date[2]}')
print('What birth date you want to know?')
user_name = input('Enter a name: ')
if user_name in date:
    print(user_name, birthday[user_name])
else:
    print(f'Not found: {user_name}')