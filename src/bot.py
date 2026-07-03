import telebot
from telebot import types
import requests
import base

bot = telebot.TeleBot(base.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(
        "Show Ads",
        callback_data='show_ads'
    )

    button2 = types.InlineKeyboardButton(
        "Show Prices",
        callback_data='show_prices'
    )

    button3 = types.InlineKeyboardButton(
        "Save DB",
        callback_data='save_db'
    )

    button4 = types.InlineKeyboardButton(
        "Show DB",
        callback_data='show_db'
    )
    
    button5 = types.InlineKeyboardButton(
    'Stats',
    callback_data='stats'
    )

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)

    bot.send_message(
        message.chat.id,
        "Choose:",
        reply_markup=markup
    )

@bot.message_handler(commands=['help'])
def help(message):

    text = '''
Commands

/start
/help
/search keyword
'''

    bot.send_message(message.chat.id, text)
    
    
@bot.message_handler(commands=['search'])
def search(message):

    temp = message.text.split(maxsplit=1)

    if len(temp) < 2:

        bot.send_message(message.chat.id, 'Enter Keyword')

        return

    keyword = temp[1]

    response = requests.get(
        f'http://127.0.0.1:8000/search/{keyword}'
    )

    data = response.json()

    if len(data) == 0:

        bot.send_message(message.chat.id, 'Not Found')

    else:

        for item in data:

            text = f'''
Title : {item["title"]}

Price : {item["price"]}

Link : {item["link"]}
'''

            bot.send_message(message.chat.id, text)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    try:

        # -----------------------------
        if call.data == 'show_ads':

            response = requests.get('http://127.0.0.1:8000/ads')

            data = response.json()

            ads = data['ads']

            for item in ads[:10]:

                text = f"""
Title : {item['title']}

Price : {item['price']}

Link : {item['link']}
"""

                bot.send_message(call.message.chat.id, text)

        # -----------------------------
        elif call.data == 'show_prices':

            response = requests.get('http://127.0.0.1:8000/ads')

            data = response.json()

            ads = data['ads']

            for item in ads[:10]:

                bot.send_message(
                    call.message.chat.id,
                    f"{item['title']}\nPrice : {item['price']}"
                )

        # -----------------------------
        elif call.data == 'save_db':

            requests.get('http://127.0.0.1:8000/save')

            bot.send_message(
                call.message.chat.id,
                "Saved"
            )
            
        # -----------------------------

        elif call.data == 'stats':
    
            response = requests.get(
                'http://127.0.0.1:8000/stats'
            )

            data = response.json()

            bot.send_message(
                call.message.chat.id,
                f'Total Ads : {data["count"]}'
            )

        # -----------------------------
        elif call.data == 'show_db':

            response = requests.get('http://127.0.0.1:8000/database')

            data = response.json()

            if len(data) == 0:

                bot.send_message(
                    call.message.chat.id,
                    "Empty"
                )

            else:

                for item in data[:10]:

                    text = f"""
ID : {item['id']}

Title : {item['title']}

Price : {item['price']}

Link : {item['link']}
"""

                    bot.send_message(call.message.chat.id, text)

    except Exception as e:

        bot.send_message(
            call.message.chat.id,
            str(e)
        )

@bot.message_handler(commands=['item'])
def item(message):

    temp = message.text.split()

    if len(temp) < 2:

        bot.send_message(message.chat.id,'Enter ID')

        return

    response = requests.get(
        f'http://127.0.0.1:8000/item/{temp[1]}'
    )

    bot.send_message(
        message.chat.id,
        str(response.json())
    )

print("Bot Started...")

bot.infinity_polling()