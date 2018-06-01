from datetime import date, timedelta
dt = date(2000, 1, 1)
print(dt)

delta = timedelta(days=1) #zdes lejit odin den
print(delta)

print(dt - delta)
print(dt + delta)