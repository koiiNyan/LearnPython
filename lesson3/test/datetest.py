from datetime import datetime
date = datetime.now()
print(date)

date2 = datetime(2015, 5, 16, 8, 3, 44) #year month day hours minutes sec
print(date2)

delta = date - date2
print(delta)

date3 = delta + date2
print(date3)