def ask_user():
    while True:
        user_say = input('Как дела? ')
        if user_say.lower() == 'хорошо':
            break
    else:
        user_say = input('Как дела? ')

ask_user()