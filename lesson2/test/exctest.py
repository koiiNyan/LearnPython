def cut_cake(parts):
    try:
        parts = int(input("Number: "))
        result = 1/parts
        return result
    except ZeroDivisionError:
        return "Can't divide by zero"
    except (TypeError, ValueError):
        return "Give me a number, please! :c"


print(cut_cake(input))