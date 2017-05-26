import random
import re
import requests

from Bot import constants
from Bot.excuses import first, second, third, fourth, smiles, funny_categories

end_of_message = "...так что сегодня я пасс "
bing_img_link = 'https://www.bing.com/images/search?q='
anya_alina_photo = 'https://media0.giphy.com/media/UtEviWeCw7tx6/200.webp#14-grid1'
bing_pattern = 'div.class\=\"ite.*?href=\"(.*?)\"'


def get_good_otmazka():
    search_message = __get_second_part()
    prepared_answer = __get_first_part() + search_message + __get_third_part() + __get_fourth_part() + end_of_message + random.choice(
        smiles.message)
    random_time_answer = random.randint(0, 3)
    picture = __pic(search_message)
    return {'message': prepared_answer, 'time': random_time_answer, 'pic': picture}


def __pic(msg):
    try:
        ss = requests.Session()
        r = ss.get(bing_img_link + msg)
        p = bing_pattern
        response = r.text
        w = re.findall(p, response)
        if len(w) > 15:
            # Первые 20 фото
            w = w[0:14:1]
            return random.choice(w)
        else:
            return anya_alina_photo
    except requests.exceptions.BaseHTTPError:
        print('Ooops, somthing happend with request')

def __get_first_part():
    return random.choice(first.message)


def __get_second_part():
    return random.choice(second.message)


def __get_third_part():
    return random.choice(third.message)


def __get_fourth_part():
    return random.choice(fourth.message)


def __get_funny_category():
    return random.choice(funny_categories.message)