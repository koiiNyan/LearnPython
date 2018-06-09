from bs4 import BeautifulSoup

from req import get_html

html = get_html('https://yandex.ru/search/?lr=10742&text=python')


if html:
    bs = BeautifulSoup(html, 'html.parser')

    #print(bs.prettify())


    #print(bs.title)
    #print(bs.title.text) #bez tega
    #for par in bs.find_all('p'): #for loop po vsem p
    #    print(par.text.upper())


    data = []


    for item in bs.find_all('li', class_='serp-item'):
        block_title = item.find('a', class_='organic__url')
        href = item.find('a', class_='path__item')

        data.append({
            'title': block_title.text,
            'link' : href.get('href')
            })



    print(data)

else:
    print('Что-то пошло не так..')