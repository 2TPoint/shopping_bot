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
                         f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакты моих разработчиков: @skylejke, @wJexson',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул вас в главное меню', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


@bot.message_handler()
def get_info(message):
    if message.text == "📄 О боте":
        info = "Информация о боте"
        bot.send_message(message.chat.id, info, parse_mode='html')
    elif message.text == "🛍 Товары":
        info = "Информация о товарах"
        bot.send_message(message.chat.id, info, parse_mode='html')
    elif message.text == "⚙ Поддержка":
        info = "Обработка обращения"
        bot.send_message(message.chat.id, info, parse_mode='html')
    else:
        bot.send_message(message.chat.id, wrong_answers[random.randint(0, 3)])


bot.polling(none_stop=True)
