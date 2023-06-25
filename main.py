from countryinfo import CountryInfo
import telebot
from configuration import*
from telebot import types

country =CountryInfo("Israel")

capital = country.capital()
area = country.area()
borders = country.borders()
flag = country.flag()
currencies = country.currencies()

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)


    #Keybboard
    btn1 = types.InlineKeyboardButton('Capital', callback_data='capital')
    btn2 = types.InlineKeyboardButton('Area', callback_data='area')
    btn3 = types.InlineKeyboardButton('Borders', callback_data='borders')
    btn4 = types.InlineKeyboardButton('Currencies', callback_data='currencies')
    btn5 = types.InlineKeyboardButton('Flag', callback_data='flag')

    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, '''
        just send country markup

    
    ''', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.text == 'capital':
        bot.send_message(call.chat.id, capital)
    elif call.text == 'area':
        bot.send_message(call.chat.id, area)
    elif call.text == 'borders':
        bot.send_message(call.chat.id, borders)
    elif call.text == 'currencies':
        bot.send_message(call.chat.id, currencies)
    elif call.text == 'flag':
        bot.send_message(call.chat.id, flag)
    


bot.polling(none_stop=True)








""" print(country.name())
print('-'*100)
print(country.capital())
print('-'*100)
print(country.area())
print('-'*100)
print(country.borders())
print('-'*100)
print(country.currencies())
print('-'*100)
print(country.flag())
print('-'*100)
print(country.languages())
print('-'*100)
print(country.region())
print('-'*100)
print(country.subregion())
print('-'*100)
print(country.population())
print('-'*100)
print(country.timezones())
print('-'*100)
print(country.native_name())
print('-'*100)
print(country.iso())
print('-'*100)
print(country.provinces())

"""

