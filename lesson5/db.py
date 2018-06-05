from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey 
#ForeignKey- vnesniyi kluch, otvechaet za svyaz s drugimi tablicami

from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()


#Opisanie tablici

class User(Base): #class User nasleduetsya ot klassa Base, obladaet vsemi vozmojnostyami klassa Base
    __tablename__ = 'users' #atribut tablename - kak v bd nazvat tablicu
    
    #Sozdaem kolonki(stolbiki) dlya tablici
    id = Column(Integer, primary_key=True) #pk true - id budet pervichnim kluchom, vsegda k id pribavlyat primary key!!
    first_name = Column(String(50)) #String 50 - dlina stroki, ogranichenie
    last_name = Column(String(50))
    email = Column(String(120), unique=True) #unique - bd budet sama delat proverku na unikalnost email
                                             #//ne doljno bit 2 userov s odinakovim email, pri popitchke sozdat usera
                                             #s takim je email,  BD vernet oshibku, chhto email uje est'


    posts = relationship('Post', backref='author')




#OB'YAVLYAEM FUNKTSII VNUTRI CLASSA (METOD)

    #Konstruktor klassa
    #Opisivaem abstraktnogo usera, kotoriy mojet bit lubim
    #Kajdii raz, kogda budem sozdavat potomka usera, budet avtomaticheski sozdavatsya init
    def __init__(self, first_name=None, last_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    #Print the data from db
    def __repr__(self):
        return '<User {} {} {}'.format(self.first_name, self.last_name, self.email)





class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    image = Column(String(500))
    published = Column(DateTime)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id')) #Svyazivaem posts s user po kolonke id


    def __init__(self, title=None, image=None, published=None, content=None, user_id=None):
        self.title = title
        self.image = image
        self.published = published
        self.content = content
        self.user_id = user_id


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)