from datetime import date, timedelta

current = date.today()
print("Today is {}!".format(current))

one_day = timedelta(days=1)

yesterday = current - one_day
print("Yesterday was {}!".format(yesterday))

tomorrow = current + one_day
print("Tomorrow will be {}!".format(tomorrow))

month = timedelta(days=30)

next_month = current + month
print("Next month will be {}!".format(next_month))

last_month = current - month
print("Last month was {}!".format(last_month))