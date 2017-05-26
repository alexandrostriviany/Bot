import re
import random
from urllib import parse

import requests

default = 'http://media0.giphy.com/media/tSxNIzbfeizrW/giphy.gif'
bing_img_link = 'https://www.bing.com/images/search?q='
bing_pattern = 'div.class\=\"ite.*?href=\"(.*?)\"'
foursquare_pattern = 'div.class\=\"venueNam.*?href=\"(.*?)\"'
foursquare_price_pattern = 'span.class\=\"price.*?title=\"(.*?)\"'
foursquare_venue_directions = 'span.class\=\"venueDirectionsLink.*?href=\"(.*?)\"'
foursquare_link = "https://ru.foursquare.com/explore?mode=url&near=%D0%9A%D0%B8%D0%B5%D0%B2%2C%20%D0%A3%D0%BA%D1%80%D0" \
                  "%B0%D0%B8%D0%BD%D0%B0&nearGeoId=72057594038631384&price=2&q=Bars"
keyword = ['drink', 'party', 'drunk girls']


def random_bar_info():
    bar_info = __get_bar_info()
    bar_name = bar_info.get('name').upper()
    bar_location = __parse_location(bar_info.get('location'))
    cost = __cost_translater(bar_info.get('cost'))
    return {'bar_name': bar_name, 'cost': cost, 'latitude': bar_location.get('latitude'),
            'longitude': bar_location.get('longitude'), 'gif': __pic()}


def __parse_location(google_map_link):
    location = google_map_link.split('=')[1].split(',')
    return {'latitude': location[0], 'longitude': location[1]}


def __get_bar_info():
    bar = __get_random_bar()
    bar_name = parse.unquote(bar.split('/')[2].replace('-', ' '))
    foursquare_id = bar.split('/')[3]
    start_session = requests.Session()
    response = start_session.get("https://ru.foursquare.com" + bar).text
    bar_location = re.findall(foursquare_venue_directions, response)[0]
    cost = re.findall(foursquare_price_pattern, response)[0]
    list = {'name': bar_name, 'location': bar_location, 'foursquare_id': foursquare_id, 'cost': cost}
    return list


def __cost_translater(comment):
    if type(comment) == str:
        if comment == 'С умеренными ценами':
            return 'Дохуя, но можно позволить $$'
        elif comment == 'Дешевое':
            return 'Хуйня для нищебродов - наш формат $'
        elif comment == 'Дорого':
            return 'Вообще дохуя, на сыры не останется $$$'
        elif comment == 'Очень дорогое':
            return 'Вода без газа по цене почки $$$$'
    else:
        return 'Ценовая категория хз'


def __get_random_bar():
    start_session = requests.Session()
    response = start_session.get(foursquare_link).text
    bar_list = re.findall(foursquare_pattern, response)
    if len(bar_list) > 0:
        return random.choice(bar_list)


def __pic():
    try:
        ss = requests.Session()
        r = ss.get(bing_img_link + random.choice(keyword) + ' gif')
        p = bing_pattern
        response = r.text
        w = re.findall(p, response)
        if len(w) > 20:
            # Первые 20 фото
            w = w[0:14:1]
            return random.choice(w)
        else:
            return default
    except:
        print('Ooops, smth happened with request')
