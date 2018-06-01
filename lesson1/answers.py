def get_answer(question, answers):
    question = question.lower()
    return answers.get(question, "Ошибка")



answers = {
    "привет": "И тебе привет!",
    "как дела": "Лучше всех", 
    "пока": "Увидимся"
    }

x = input("Привет. ")
result = get_answer(x, answers)
print(result)

y = input("Как дела? ")
result2 = get_answer(y, answers)
print(result2)

z = input("Пока ")
result3 = get_answer(z, answers)
print(result3)