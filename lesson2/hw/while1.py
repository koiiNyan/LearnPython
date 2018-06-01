names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
person = "Валера"
while True:
    if names.pop() == person:
        print("Валера нашелся.")
        break
    else:
        print("Валера потерялся!")