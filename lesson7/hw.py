""" Code to change

import json
statii = json.load(open('articles.json', 'r'))
p=2
s = 5
i=0
while i < 100:
    if (i >= (p-1) * s) and (i <= p*s): print statii[i]
    i = i + 1 

"""

"""
I VAR:

import json
articles = json.load(open('articles.json', 'r'))
page_num = 2
articles_on_page = 5
first_index = (page_num - 1) * articles_on_page
last_index = page_num * articles_on_page
for article in articles[first_index:last_index]:
    print(article)

"""


# Загрузка данных из файла
# Фильтрация статей
# Вывод нужных статей

# BETTER VAR:

import json

def load_data(filepath):
    return json.load(open('filepath', 'r'))

def filter_data(articles, page_num, articles_on_page):
    first_index = (page_num - 1) * articles_on_page
    last_index = page_num * articles_on_page
    return articles[first_index:last_index]

def print_articles(articles):
    for article in articles:
        print(article)


if __name__ == "__main__":
    articles = load_data('articles.json')
    articles_on_page = filter_data(articles=articles, page_num=2, articles_on_page=5)
    print_articles(articles_on_page)