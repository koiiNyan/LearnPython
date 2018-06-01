users = {
    'Name1' : {'city' : 'Moscow', 'temperature': '20', 'wind': 'west'},
    'Name2' : {'city' : 'Spb', 'temperature': '16', 'wind': 'north'},
    'Name3' : {'city' : 'Tver', 'temperature': '10', 'wind': 'south'}
}

name = input('Your name? ')
print(name)

user = users.get(name)

if user:
    print(user['city'], user['temperature'], user['wind'])

else:
    print('Not found')