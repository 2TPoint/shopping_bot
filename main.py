import random
import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6239002249:AAFzUiVsQNdwbkASuxub9Pj37vxjlB1Tr7I')

wrong_answers = ['Я не понял, что ты хочешь сказать', 'Извини, я тебя не понимаю', 'Я не знаю такой команды',
                 'Мой разработчик не говорил, что отвечать в такой ситуации -_-']


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    products_button = types.KeyboardButton("🛍 Товары")
    about_button = types.KeyboardButton("📄 О боте")
    support_button = types.KeyboardButton("⚙ Поддержка")
    markup.row(products_button)
    markup.row(about_button, support_button)
    if message.text == '/start':
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name}!\nЯ телеграм-бот для покупок\nУ меня ты сможешь купить некоторые товары!\nКонтакты моих разработчиков: @skylejke, @wJexson',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул вас в главное меню', reply_markup=markup)


@bot.message_handler()
def get_info(message):
    if message.text == "📄 О боте":
        aboutChapter(message)
    elif message.text == "🛍 Товары":
        productsChapter(message)
    elif message.text == "⚙ Поддержка":
        supportChapter(message)
    elif message.text == '🔹 Товар №1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о первом товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар №2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о втором товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар №3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о третьем товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар №4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о четвертом товаре...', reply_markup=markup)
    elif message.text == '✏ Написать разработчику':
        bot.send_message(message.chat.id, '<b>Контакты моих разработчиков:</b> @skylejke, @wJexson', parse_mode='html')
    elif message.text == '💳 Купить':
        seller = random.randint(0, 1)
        if seller == 0:
            webbrowser.open('https://t.me/skylejke')
        elif seller == 1:
            webbrowser.open('https://t.me/wJexson')
    elif message.text == '↩ Назад':
        productsChapter(message)
    elif message.text == '↩ Назад в меню':
        start(message)
    else:
        bot.send_message(message.chat.id, wrong_answers[random.randint(0, 3)])


def productsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Товар №1')
    button2 = types.KeyboardButton('🔹 Товар №2')
    button3 = types.KeyboardButton('🔹 Товар №3')
    button4 = types.KeyboardButton('🔹 Товар №4')
    button5 = types.KeyboardButton('↩ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Раздел товаров', reply_markup=markup)


def aboutChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩ Назад в меню')
    markup.add(button1)
    bot.send_message(message.chat.id, 'Я телеграм-бот для покупок\nУ меня ты сможешь купить некоторые товары!',
                     reply_markup=markup)


def supportChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton('✏ Написать разработчику')
    button2 = types.KeyboardButton('↩ Назад в меню')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Раздел поддержки', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


bot.polling(none_stop=True)
