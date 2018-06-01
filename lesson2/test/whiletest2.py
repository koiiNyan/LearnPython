while True:
    user_say = input('Say smth: ')
    if user_say == 'Bye' or user_say == 'bye':
        print('Bye -.-')
        break
    else:
        print('You are {}'.format(user_say))