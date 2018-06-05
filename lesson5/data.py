from db import User

u = User
print(u)

#Poluchaem dannie iz db
print(u.query.all())


#FILTR PO PERVOMU IMENI, first - pervoe sovpadenie
m = u.query.filter(User.first_name=='Маша').first()
print(m)
print(m.id)


#FILTR PO SOVPADENIU
all_m = u.query.filter(User.first_name.like('М%')).all()  
#M% - pervaya bukva M, posle nee - luboe kol-vo lubix simbolov
print(all_m)


#SORTING

#А-Я PO VOZRASTANIU

sorta = u.query.order_by(User.email).all()
print(sorta)

#Я-А PO UBIVANIU
sortb = u.query.order_by(User.email.desc()).all()
print(sortb)


#ОБЪЕДИНЕНИЕ МЕТОДОВ
sort = u.query.filter(User.last_name.like('%ов%')).order_by(User.first_name).all()
print(sort)
