import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
import selenium_func

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton(text='Парсер по артикулу', callback_data='artikul'))
    markup.add(types.InlineKeyboardButton(text='Парсер по ссылке', callback_data='link'))

    bot.send_message(message.from_user.id, text=config.start_message, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def pars(call):
    if call.data == 'artikul':
        artikul = bot.send_message(call.from_user.id, text='Введите артикул товара WB: ')
        bot.register_next_step_handler(artikul, artikul_func)

    if call.data == 'link':
        link = bot.send_message(call.from_user.id, text='Введите ссылку товара WB: ')
        bot.register_next_step_handler(link, link_func)

def artikul_func(message):
    art = message.text

    selenium_func.artikul_selenium_func('https://www.wildberries.ru/catalog/' + art + '/detail.aspx')

    img = open('filename.png', 'rb')
    bot.send_photo(message.chat.id, img)

def link_func(message):
    links = message.text

    selenium_func.artikul_selenium_func(links)
    
    img = open('filename.png', 'rb')
    bot.send_photo(message.chat.id, img)

bot.polling(non_stop=True)