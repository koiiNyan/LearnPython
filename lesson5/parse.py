from bs4 import BeautifulSoup

from req import get_html

html = get_html('https://yandex.ru/search/?lr=10742&text=python')


bs = BeautifulSoup(html, 'html.parser')

#print(bs.prettify())


#print(bs.title)
#print(bs.title.text) #bez tega
#for par in bs.find_all('p'): #for loop po vsem p
#    print(par.text.upper())

for item in bs.find_all('li', class_='serp-item'):
    block_title = item.find('a', class_='organic__url')
    print(block_title.text)
    href = item.find('a', class_='path__item')
    print(href)
    
