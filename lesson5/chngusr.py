from db import db_session, User

from addusr import me

me.email='anovinnikova@yandex.ru'
db_session.commit()