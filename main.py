import random
import telebot
import openpyxl
from telebot import types


class Product:
    def __init__(self, name, description, price, link):
        self.name = name
        self.description = description
        self.price = price
        self.link = link


def get_products():
    # Загрузка данных из Excel-файла
    workbook = openpyxl.load_workbook("products.xlsx")
    worksheet = workbook.active

    # Создание списка для хранения объектов товаров
    products = []

    # Итерация по строкам таблицы и создание объектов Товар
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        name = row[0]
        description = row[1]
        price = row[2]
        link = row[3]

        product = Product(name, description, price, link)
        products.append(product)

    return products
    # # Вывод полученных данных
    # for product in products:
    #     print(f"Название: {product.name}")
    #     print(f"Описание: {product.description}")
    #     print(f"Цена: {product.price}")
    #     print(f"Ссылка: {product.link}")
    #     print()


products = get_products()

bot = telebot.TeleBot('6239002249:AAFzUiVsQNdwbkASuxub9Pj37vxjlB1Tr7I')  # Инициализация бота

# Список, содержащий ответы бота на неизвестные команды
wrong_answers = ['Я не понял, что ты хочешь сказать', 'Извини, я тебя не понимаю', 'Я не знаю такой команды',
                 'Мой разработчик не говорил, что отвечать в такой ситуации -_-']


@bot.message_handler(commands=['start'])
def start(message):
    """
    Обрабатывает команду '/start' от пользователя:
           1. Запускает бота
           2. Создает клавиатуру для главного меню
           3. Выводит приветствующий текст
    :param message: сообщение от пользователя
    :return: ничего не вовзращает
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    products_button = types.KeyboardButton("🛍 Товары")
    about_button = types.KeyboardButton("📄 О боте")
    support_button = types.KeyboardButton("⚙ Поддержка")
    markup.row(products_button)
    markup.row(about_button, support_button)
    if message.text == '/start':
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name}!\nЯ телеграмм-бот для покупок\nC помощью меня вы '
                         f'сможете купить некоторые товары!\nКонтакты моих разработчиков: @skylejke, @wJexson',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул вас в главное меню', reply_markup=markup)


# Создаем словарь для хранения выбранных товаров для каждого пользователя
selected_products = {}


@bot.message_handler()
def get_info(message):
    """
    Обрабатывает текст, присланный пользователем
    В завимости от текста вызывает соответствующие методы
    :param message: сообщение от пользователя
    :return: ничего не возвращает
    """
    if message.text == "📄 О боте":
        about_chapter(message)
    elif message.text == "🛍 Товары":
        products_chapter(message)
    elif message.text == "⚙ Поддержка":
        support_chapter(message)
    elif message.text.startswith('🔹 Товар №'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩ Назад')
        markup.row(button1, button2)
        product = random.choice(products)
        selected_products[message.chat.id] = product  # Сохраняем выбранный товар для данного пользователя
        info = f"Название: {product.name}\nОписание: {product.description}\nЦена: {product.price} руб."
        bot.send_message(message.chat.id, "Информация о товаре:\n" + info, reply_markup=markup)
    elif message.text == '💳 Купить':
        product = selected_products.get(message.chat.id)  # Получаем выбранный товар для данного пользователя
        if product:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, "Ссылка на товар:\n" + product.link, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Выберите товар сначала.")
    elif message.text == '✏ Написать разработчику':
        bot.send_message(message.chat.id, '<b>Контакты моих разработчиков:</b> @skylejke, @wJexson', parse_mode='html')
    elif message.text == '↩ Назад':
        if len(selected_products) == 0:
            products_chapter(message)
        else:
            del selected_products[message.chat.id]  # Удаляем выбранный товар для данного пользователя
            products_chapter(message)
    elif message.text == '↩ Назад в меню':
        start(message)
    else:
        bot.send_message(message.chat.id, wrong_answers[random.randint(0, 3)])


# Раздел товаров
def products_chapter(message):
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


# Раздел информации о боте
def about_chapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩ Назад в меню')
    markup.add(button1)
    bot.send_message(message.chat.id,
                     'Я телеграмм-бот для покупок\nC помощью меня вы сможете узнать информацию о выгодных товарах и приобрести их!',
                     reply_markup=markup)


# Раздел поддержки
def support_chapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton('✏ Написать разработчику')
    button2 = types.KeyboardButton('↩ Назад в меню')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Раздел поддержки', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    """
    Обрабатывает фото, присланное пользователем
    :param message: сообщение от пользователя
    :return: ничего не вовзращает
    """
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


bot.polling(none_stop=True)  # Бесконечная работа бота
