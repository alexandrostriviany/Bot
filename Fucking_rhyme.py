import random

import re

rhymes_dictionary = {
    "300": ["отсоси у тракториста"],
    "нет": ["пидора ответ", "говна тебе пакет"],
    "да": ["пизда"],
    "триста": ["отсоси у тракториста"],
    "смысле": ["в коромысле"],
    "че": ["хер через плечё"],
    "а": ["хуй на"],
    "шо": ["капшо"],
}


def send_rhyme(message, bot):
    word = str.split(re.sub(r'[\W]', ' ', message.text).strip(), ' ')
    word.reverse()
    if len(word) > 0:
        word = word[0]
        if word in rhymes_dictionary:
            return random.choice(rhymes_dictionary[word])
