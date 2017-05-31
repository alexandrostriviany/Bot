import random

boyan_imgs = ['http://lurkmore.so/images/0/03/Breshko-Breshkovskaya-1917-Bayan.jpg',
              'http://lurkmore.so/images/9/9c/BayanC2.jpg',
              'http://s.pikabu.ru/post_img/2014/01/12/10/1389546095_1278526281.jpg',
              'https://i.ytimg.com/vi/liEOWKB5lzA/maxresdefault.jpg',
              'http://lurkmore.so/images/6/61/Starik_boyanich.jpg']

boyan_gifs = ['https://s01.yapfiles.ru/files/1249645/bayangifkifuturama154488.gif',
              'http://cs.pikabu.ru/images/big_size_comm/2013-05_6/13696211679739.gif',
              'http://eosof.ru/_ph/10/2/58493839.gif',
              'https://s02.yapfiles.ru/files/1088376/BAYaN.gif',
              'http://cs3.pikabu.ru/images/big_size_comm_an/2014-02_3/13924678862314.gif']

boyan_creators = ['diegowithfourteeno','Алина']
checker = [False, True, False]


def send_boyan(message, bot):
    isBoyan = random.choice(checker)
    if 'http' in message.text and isBoyan:
        if random.choice(checker):
            bot.send_photo(message.chat.id, random.choice(boyan_imgs))
        else:
            bot.send_document(message.chat.id, random.choice(boyan_gifs))
