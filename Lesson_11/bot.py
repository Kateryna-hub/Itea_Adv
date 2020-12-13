from config import TOKEN
from telebot import TeleBot
from telebot.types import Message
import sqlite3
from sqlite3 import Error

bot = TeleBot(TOKEN)


S_START = 0  # What's your last name?
S_ENTER_NAME = 1  # What's your first name?
S_ENTER_PHONE = 2  # What's your phone?
S_ENTER_email = 3  # What's your email?
S_ENTER_address = 4  # What's your address?
S_ENTER_wishes = 5  # Enter your wish


def get_sql(sql):
    with sqlite3.connect('bot.db') as db:
        cursor = db.cursor()
        try:
            cursor.execute(sql)
        except Error:
            pass
        result = cursor.fetchone()
        return result


def post_sql(sql):
    with sqlite3.connect('bot.db') as db:
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)


def check_user(user_id):
    user_check_query = f'SELECT telegram_id FROM users WHERE telegram_id = {user_id}'
    user_check_data = get_sql(user_check_query)
    if not user_check_data:
        return None
    else:
        return user_check_data


def get_chat_id(user_id):
    chat_id_query = f'SELECT chat_id FROM users WHERE telegram_id = {user_id}'
    user_chat_id = get_sql(chat_id_query)
    return user_chat_id[0]


def set_chat_id(user_id, state):
    chat_id_query = f'UPDATE users SET chat_id = "{state}" WHERE telegram_id = "{user_id}"'
    post_sql(chat_id_query)


@bot.message_handler(commands=['start'])
def handle_start(message):
    m_id = str(message.from_user.id)
    m_username = f'"{message.from_user.username}"'
    if check_user(m_id) is None:
        insert_to_db = f'INSERT INTO users (telegram_id,username,surname,first_name,phone,email,address,chat_id) ' \
                       f'VALUES ({m_id}, {m_username}, "None", "None", 0, "None", "None", {S_START})'
        post_sql(insert_to_db)
        bot.send_message(
            message.chat.id,
            f"Hello, {message.from_user.first_name}.\nWhat's your last name?"
        )
    else:
        bot.send_message(message.chat.id, "Enter your wish")
        set_chat_id(message.chat.id, S_ENTER_wishes)


@bot.message_handler(func=lambda message: get_chat_id(message.chat.id) == S_START)
def user_entering_name(message):
    text = f'"{message.text}"'
    insert_to_db = f'UPDATE users SET surname = {text} WHERE  telegram_id = {message.chat.id}'
    post_sql(insert_to_db)
    bot.send_message(message.chat.id, "What's your first name?")
    set_chat_id(message.chat.id, S_ENTER_NAME)


@bot.message_handler(func=lambda message: get_chat_id(message.chat.id) == S_ENTER_NAME)
def user_entering_name(message):
    text = f'"{message.text}"'
    update_to_db = f'UPDATE users SET first_name = {text} WHERE  telegram_id = {message.chat.id}'
    post_sql(update_to_db)
    bot.send_message(message.chat.id, "What's your phone?")
    set_chat_id(message.chat.id, S_ENTER_PHONE)


@bot.message_handler(func=lambda message: get_chat_id(message.chat.id) == S_ENTER_PHONE)
def user_entering_name(message):
    text = f'"{message.text}"'
    update_to_db = f'UPDATE users SET phone = {text} WHERE  telegram_id = {message.chat.id}'
    post_sql(update_to_db)
    bot.send_message(message.chat.id, "What's your email?")
    set_chat_id(message.chat.id, S_ENTER_email)


@bot.message_handler(func=lambda message: get_chat_id(message.chat.id) == S_ENTER_email)
def user_entering_name(message):
    text = f'"{message.text}"'
    update_to_db = f'UPDATE users SET email = {text} WHERE  telegram_id = {message.chat.id}'
    post_sql(update_to_db)
    bot.send_message(message.chat.id, "What's your address?")
    set_chat_id(message.chat.id, S_ENTER_address)


@bot.message_handler(func=lambda message: get_chat_id(message.chat.id) == S_ENTER_address)
def user_entering_name(message):
    text = f'"{message.text}"'
    update_to_db = f'UPDATE users SET address = {text} WHERE  telegram_id = {message.chat.id}'
    post_sql(update_to_db)
    bot.send_message(message.chat.id, "Enter your wish")
    set_chat_id(message.chat.id, S_ENTER_wishes)


@bot.message_handler(func=lambda message: get_chat_id(message.chat.id) == S_ENTER_wishes)
def user_entering_name(message):
    text = f'"{message.text}"'
    update_to_db = f'INSERT INTO wishes (text, telegram_id) VALUES ({text}, {message.chat.id})'
    post_sql(update_to_db)
    bot.send_message(message.chat.id, "Thank you!")
    set_chat_id(message.chat.id, S_START)


bot.polling()