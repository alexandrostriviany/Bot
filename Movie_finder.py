from datetime import datetime, date, time
import time
import requests
from flask import json

today_data = int(datetime.timestamp(datetime.utcnow()))  # 1473897600 1473916172.49391





def get_responce():
    payload = 'sort=rate'
    r = requests.post("http://kinoafisha.ua/ajax/kinoafisha_load", data=payload)
    json_string = json.dumps(r.json())
    return json.loads(json_string)

parsed_string = get_responce()

def get_movie_name(index):
    return parsed_string['result'][index]['name']


def get_country_info(index):
    return parsed_string['result'][index]['countries']

def get_film_cover(i):
    return 'http://kinoafisha.ua' + parsed_string['result'][i]['image']

def get_imdb_rate(index):
    rate = parsed_string['result'][index]['imdb']
    if type(rate) is str:
        return float(rate.replace(",", "."))
    else: return 0
