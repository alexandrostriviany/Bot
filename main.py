#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time  # Представляет время в читаемый формат
from datetime import datetime

import telebot
from flask import Flask, request

import Bar_finder
import Fucking_rhyme
import Movie_finder
import Otmazka_creator
import constants
from excuses import smiles

server = Flask(__name__)

bot = telebot.TeleBot(constants.token)
print(bot.get_me())
counter = 0


def log(message, answer):
    print("\n -------------------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print("Ответ - " + answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, constants.help_message)


@bot.message_handler(commands=['alinahelpme'])
def send_good_otmazka(message):
    log(message, 'alinahelp')
    perfect_answer = Otmazka_creator.get_good_otmazka()
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(perfect_answer.get('time'))
    bot.send_message(message.chat.id, perfect_answer.get('message'))


@bot.message_handler(commands=['gotothebar'])
def send_bar(message):
    bar = Bar_finder.random_bar_info()
    bot.send_venue(message.chat.id, bar.get('latitude'), bar.get('longitude'), bar.get('bar_name'), bar.get('cost'))
    bot.send_document(message.chat.id, bar.get('gif'))


@bot.message_handler(commands=["keyboard"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/gotothebar')
    user_markup.row('/alinahelpme')
    user_markup.row('/anyagotocinema')
    bot.send_message(message.chat.id, "(づ｡◕‿‿◕｡)づ", reply_markup=user_markup)


@bot.message_handler(commands=['anyagotocinema'])
def handle_text(message):
    i = j = 0
    while j < 10:
        if Movie_finder.get_imdb_rate(i) >= 7:
            movie = "<b>" + Movie_finder.get_movie_name(i) + "</b>" + ", " \
                    + "<i>" + Movie_finder.get_country_info(i) + "</i>" + ", " \
                    + "imdb " + "<b>" + str(Movie_finder.get_imdb_rate(i)) + "</b>"
            bot.send_photo(message.chat.id, Movie_finder.get_film_cover(i))
            bot.send_message(message.chat.id, movie, parse_mode='HTML')
            j += 1
        i += 1
    time.sleep(5)
    bot.send_message(message.chat.id, "хотя ....нет, отмена " + smiles.no_good_gesture)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, constants.start_message)


@bot.message_handler(content_types=['text'])
def send_rhyme(message):
    bot.send_message(message.chat.id, Fucking_rhyme.send_rhyme(message))


# Получение сообщений
@server.route("/", methods=['POST'])
def get_message():
    # Чтение данных от серверов telegram
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message
         ])
    return "!", 200


# Установка webhook
@server.route("/")
def webhook():
    bot.remove_webhook()
    # Если вы будете использовать хостинг или сервис без https
    # то вам необходимо создать сертификат и
    # добавить параметр certificate=open('ваш сертификат.pem')
    bot.set_webhook(url=constants.webhook)
    return "App is OK!", 200


# Запуск сервера
server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

# bot.polling(none_stop=True)
