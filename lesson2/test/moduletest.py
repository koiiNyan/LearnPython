import datetime
date = datetime.datetime.now()
print(date)
print(date.strftime('%d.%m.%Y')) #predstavlyaem datu v formate d-m-y
print(datetime.date.today())
print(date.strftime('%d/%m/%Y'))
print(date.strftime('%d.%m.%Y, %d %B, %A'))