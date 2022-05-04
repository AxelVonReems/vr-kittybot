import logging
import os

import requests

from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


DOG_URL = 'https://api.thedogapi.com/v1/images/search'
CAT_URL = 'https://api.thecatapi.com/v1/images/search'
SAMOYED_URL = 'https://dog.ceo/api/breed/samoyed/images/random'
JRT_URL = 'https://dog.ceo/api/breed/terrier/russell/images/random'
BIRD_URL = 'https://some-random-api.ml/img/birb'


DOG_TEXT = 'Хочу собачку'
CAT_TEXT = 'Хочу котика'
SAMOYED_TEXT = 'Хочу самоеда'
JRT_TEXT = 'Хочу курьерчика'
BIRD_TEXT = 'Хочу птичку'
PLANT_TEXT = 'Хочу растение'


BUTTONS = [
    [KeyboardButton(DOG_TEXT), KeyboardButton(CAT_TEXT)],
    [KeyboardButton(SAMOYED_TEXT), KeyboardButton(BIRD_TEXT)],
    [KeyboardButton(JRT_TEXT)]
    ]


def get_dog_image():
    try:
        response = requests.get(DOG_URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к API с собаками: {error}')
        new_url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_pic = response[0].get('url')
    return random_pic


def get_cat_image():
    try:
        response = requests.get(CAT_URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к API с котами: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_pic = response[0].get('url')
    return random_pic


def get_samoyed_image():
    try:
        response = requests.get(SAMOYED_URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к API с самоедами: {error}')
        new_url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_pic = response.get('message')
    return random_pic


def get_jrt_image():
    try:
        response = requests.get(JRT_URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к API с самоедами: {error}')
        new_url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_pic = response.get('message')
    return random_pic


def get_bird_image():
    try:
        response = requests.get(BIRD_URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к API с самоедами: {error}')
        new_url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_pic = response.get('link')
    return random_pic


def start_bot(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=('Привет, {}. Какого зверя тебе показать?'.format(name)),
        reply_markup=ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True)
    )


def message_sender(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    if DOG_TEXT in update.message.text:
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                '{}, посмотри какую собачку я тебе нашел! Гав!'.format(name)),
            reply_markup=ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True),
        )
        context.bot.send_photo(chat.id, get_dog_image())
    if CAT_TEXT in update.message.text:
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                '{}, посмотри какого котика я тебе нашел! Гав!'.format(name)),
            reply_markup=ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True),
        )
        context.bot.send_photo(chat.id, get_cat_image())
    if SAMOYED_TEXT in update.message.text:
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                '{}, посмотри какого самоеда я тебе нашел! Гав!'.format(name)),
            reply_markup=ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True),
        )
        context.bot.send_photo(chat.id, get_samoyed_image())
    if JRT_TEXT in update.message.text:
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                '{}, посмотри какого курьерчика я тебе нашел! Гав!'.
                format(name)),
            reply_markup=ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True),
        )
        context.bot.send_photo(chat.id, get_jrt_image())
    if BIRD_TEXT in update.message.text:
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                '{}, посмотри какую птичку я тебе нашел! Гав!'.
                format(name)),
            reply_markup=ReplyKeyboardMarkup(BUTTONS, resize_keyboard=True),
        )
        context.bot.send_photo(chat.id, get_bird_image())


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', start_bot))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text, message_sender)
    )
    # updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    # updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))
    # updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


"""
def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вот тебе ещё один пёсик! Гав!',
    )
    context.bot.send_photo(chat.id, get_new_dog_image())


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вот тебе ещё один котик! Гав!',
    )
    context.bot.send_photo(chat.id, get_new_cat_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=('Привет, {}. Посмотри какого пёсика я тебе нашел! Гав!'.
              format(name)),
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_new_dog_image())
"""
