from db import db_session, User

me = User('Анастасия', 'Овинникова', 'anovinnikova@yandex.ru')

print(me)
print(me.email)

print(me.first_name)
print(me.last_name)


db_session.add(me) #dobavlyaem dannie v db
db_session.commit() #zapisivaem dannie v db
