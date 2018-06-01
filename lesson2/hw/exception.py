answers = {
    "привет": "Привет!",
    "как дела?": "Отлично, а у тебя?",
    "пока": "Еще увидимся!"
}

def get_answer(question, answers):
    return answers.get(question.lower())

def ask_user(answers):
    try:
        while True:
            user_input = input("Скажи что-нибудь: ")
            answer = get_answer(user_input, answers)
            print(answer)
            if user_input == 'пока':
                break

    except KeyboardInterrupt:
        x = print("\nБыло приятно пообщаться!")
        return x


ask_user(answers)