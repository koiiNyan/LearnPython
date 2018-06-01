
from datetime import datetime

from flask import Flask, abort, request

from req import get_weather, get_names

from news_list import all_news

city_id = 524901
apikey = 'b78478e26d96a81eaa05b7b54b4bbec6'

app = Flask(__name__) # __name__ - nazvanie tekushego faila

@app.route("/") #glavnaya stranica
#obrabativaem route
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&APPID=%s" % (city_id, apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    
    result = "<p><b>Город:</b> %s</p>" % weather['name']
    result += "<p><b>Температура:</b> %s</p>" % weather['main']['temp']
    result += "<p><b>Дата:</b> %s</p>" % cur_date
    return result


@app.route("/news")
def all_the_news():
    colors = ['green, red, blue, magenta']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit)




@app.route("/news/<int:news_id>")
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id] #vozvrashaet spisok!
    if len(news_to_show) == 1:
        result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
        result = result % news_to_show[0]
        return result
    else:
        abort(404)

@app.route("/names")
def pop_names():
    url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key=36ad703ba084d725ef8cf11e0c45c58c"
    name = get_names(url)

    result = '''<table> 
    <tr>
        <th>Имя:</th>
        <th>Год:</th>
        <th>Месяц:</th>
        <th>Кол-во человек:</th>
    </tr>'''

    for n in name:        
        result += '''<tr>
           <td>{}</td>
           <td>{}</td>
           <td>{}</td>
           <td>{}</td>
        </tr>'''.format(n['Cells']['Name'], n['Cells']['Year'], n['Cells']['Month'], n['Cells']['NumberOfPersons'])

    result += '</table>'

    
    return result


@app.route("/names/<int:year_id>")
def year_by_id(year_id):
    url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key=36ad703ba084d725ef8cf11e0c45c58c"
    name = get_names(url)
    year_to_show = [years for years in name if years['Cells']['Year'] == year_id]
    
    result = '''<table>
    <tr>
        <th>Имя:</th>
        <th>Год:</th>
        <th>Месяц:</th>
        <th>Кол-во человек:/th>'''


    for n in year_to_show:        
        result += '''<tr>
           <td>{}</td>
           <td>{}</td>
           <td>{}</td>
           <td>{}</td>
        </tr>'''.format(n['Cells']['Name'], n['Cells']['Year'], n['Cells']['Month'], n['Cells']['NumberOfPersons'])

    result += '</table>'
    return result

if __name__ == "__main__":
    app.run()



