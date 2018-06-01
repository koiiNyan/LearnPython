
import requests


def get_weather(url):
    result = requests.get(url) #string
    
    if result.status_code == 200: #check chto ststus servera ok
        return result.json() #json - perevodim str v dict (json - metod modulya requests)
    else:
        print("Что-то пошло не так")





def get_names(url):
    result = requests.get(url) 
    
    if result.status_code == 200:
        return result.json() 
    else:
        print("Что-то пошло не так")



if __name__ == "__main__":
    data = get_names("http://api.data.mos.ru/v1/datasets/2009/rows?api_key=36ad703ba084d725ef8cf11e0c45c58c")

