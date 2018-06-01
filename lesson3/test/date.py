from datetime import datetime

date = datetime.now()
print(date.strftime ('%d.%m.%Y %H:%M'))
print(date.strftime('%d %B %Y, %A'))
print(date.strftime('%A %d %B %Y'))

#poluchaem datu iz stroki
date_string = '12/23/2010'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)