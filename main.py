import telebot
from telebot import types

bot = telebot.TeleBot('6239002249:AAFzUiVsQNdwbkASuxub9Pj37vxjlB1Tr7I')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}!'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    about_button = types.KeyboardButton("О боте")
    asdproducts_button = types.KeyboardButton("Товары")
    support_button = types.KeyboardButton("Поддержка")
    personal_button = types.KeyboardButton("Личный кабинет")
    markup.add(about_button, asdproducts_button, support_button, personal_button)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler()
def get_info(message):
    if message.text == "О боте":
        info = "Информация о боте"
        bot.send_message(message.chat.id, info, parse_mode='html')
    elif message.text == "Товары":
        info = "Информация о товарах"
        bot.send_message(message.chat.id, info, parse_mode='html')
    elif message.text == "Поддержка":
        info = "Обработка обращения"
        bot.send_message(message.chat.id, info, parse_mode='html')
    elif message.text == "Личный кабинет":
        info = "Личный кабинет"
        bot.send_message(message.chat.id, info, parse_mode='html')


bot.polling(none_stop=True)
