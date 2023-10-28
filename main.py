import requests
import telebot

from datetime import datetime
from settings import TOKEN, API_URL


def get_data():
    req = requests.get(API_URL)
    response = req.json()
    # print(response)
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


def telegram_bot(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        username = message.from_user.username
        bot.send_message(message.chat.id, f"Привет @{username}, напиши 'цена' "
                                          f"и я пришлю тебе цену BTC.")


    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "цена":
            try:
                req = requests.get(API_URL)
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                    f"Цена продажи BTC: {sell_price} USD"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то пошло не так, я походу приболел :(."
                )
        else:
            bot.send_message(message.chat.id, "Проверь введённый текст! :(")

    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(TOKEN)

# def send_message():
#     print(API_KEY, DB_PASSWORD)
#
# send_message()
