def find_person(name, mylist):
    while True:
        if (name in mylist):
            print((name), "нашелся.")
        else:
            print("Not in list :p")
        break


mylist = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name = input("Name: ")
find_person (name, mylist)
