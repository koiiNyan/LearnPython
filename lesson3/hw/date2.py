from datetime import datetime

date_str = "01/01/17 12:10:03.234567"
print(date_str)
date_date = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
print(date_date)