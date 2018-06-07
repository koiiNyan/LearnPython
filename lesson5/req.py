import requests


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status() #check status
        return result.text
    except requests.exceptions.RequestException:
        print('Не получилось :c') 
        return False
