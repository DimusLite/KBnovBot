#import requests
#TOKEN = '705130797:AAGoiH-ru25oKOgAmTP1qiMNAh5wB0FBtaY'
#BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'
#r = requests.get(f'{BASE_URL}getMe')
#import pprint
#pprint.pprint(r.json())

import telebot
from telebot.types import Message
from telebot import apihelper

TOKEN = '705130797:AAGoiH-ru25oKOgAmTP1qiMNAh5wB0FBtaY'
PROXY = 'socks5://111.223.75.178:8888'

bot = telebot.TeleBot(TOKEN)
apihelper.proxy = {'https': PROXY}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func = lambda message: True)
def reply(message: Message):
    replyText = 'Сам ты ' + message.text

#======================================================
    inputMsg = message.text
    import re
    OLD_VER_LIST_KEY = "Неактуальная версия конф. 1С!"

    def MakeNumBold(msg):
        numsList = re.findall(r'№\d+', msg)
        for num in numsList:
            msg = re.sub(num, '*' + num + '*', msg)
        return msg

    if OLD_VER_LIST_KEY in inputMsg:
        replyText = MakeNumBold(inputMsg)

#======================================================
    
    bot.reply_to(message, replyText)

bot.polling()
