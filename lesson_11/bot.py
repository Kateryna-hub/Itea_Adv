from config import TOKEN
from telebot import TeleBot

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(
        message.chat.id,
        'Hello!'
    )


bot.polling()