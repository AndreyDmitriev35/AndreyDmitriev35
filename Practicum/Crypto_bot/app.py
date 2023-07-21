import telebot
from config import keys, token
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def helper(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате, через пробел:\n\
Имя валюты, цену которой Вы хотите узнать\nИмя валюты, в которой надо узнать цену первой валюты\n\
Количество первой валюты\n\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(" ")

        if len(value) != 3:
            raise APIException('Слишком много параметров.')

        base, quote, amount = value
        total_base = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        price = round(total_base*int(amount), 3)
        text = f'Цена {amount} {base} при переводе в {quote} - {price}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
