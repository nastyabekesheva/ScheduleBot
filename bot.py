import pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


from telegram.ext import *
from telegram import *
import pymongo
from pymongo import MongoClient

import datetime
import logging

cluster = MongoClient('mongodb+srv://nastyabekesheva:tkyrpl190@scheduledb.xtrt8vp.mongodb.net/?retryWrites=true&w=majority')
db = cluster['ScheduleDB']
collection = db['schedule']
users = db['users']


start_date = datetime.date(2022, 9, 5)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

updater = Updater(token='5651742670:AAGCoiS_uwqAFJ5BZFmb7kkbs7DhrwFv6W0', use_context=True)
dispatcher = updater.dispatcher
j = updater.job_queue
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

week_1_buttons = [[KeyboardButton('Понеділок (т. 1)'), KeyboardButton('Вівторок (т. 1)')], [KeyboardButton('Середа (т. 1)'), KeyboardButton('Четвер (т. 1)')], [KeyboardButton('П\'ятниця (т. 1)'), KeyboardButton('Субота (т. 1)')], [KeyboardButton('Вибрати тиждень')]]
week_2_buttons = [[KeyboardButton('Понеділок (т. 2)'), KeyboardButton('Вівторок (т. 2)')], [KeyboardButton('Середа (т. 2)'), KeyboardButton('Четвер (т. 2)')], [KeyboardButton('П\'ятниця (т. 2)'), KeyboardButton('Субота (т. 2)')], [KeyboardButton('Вибрати тиждень')]]

def parse(result_collection):
    messages = {}
    for result in result_collection:
        if result['time'] == '08:30':
            messages.update({1 : f'Пара №1\n{result["name"]}\n{result["teacher"]}\nПосилання:{result["link"]}\n\n'})
        elif result['time'] == '10:25':
            messages.update({2 : f'Пара №2\n{result["name"]}\n{result["teacher"]}\nПосилання:{result["link"]}\n\n'})
        elif result['time'] == '12:20':
            messages.update({3 : f'Пара №3\n{result["name"]}\n{result["teacher"]}\nПосилання:{result["link"]}\n\n'})
        elif result['time'] == '14:15':
            messages.update({4 : f'Пара №4\n{result["name"]}\n{result["teacher"]}\nПосилання:{result["link"]}\n\n'})
        elif result['time'] == '16:10':
            messages.update({5 : f'Пара №5\n{result["name"]}\n{result["teacher"]}\nПосилання:{result["link"]}\n\n'})
        elif result['time'] == '18:30':
            messages.update({6 : f'Пара №6\n{result["name"]}\n{result["teacher"]}\nПосилання:{result["link"]}\n\n'})
    messages = dict(sorted(messages.items()))
    message = ''.join(messages.values())
    if message == '':
        message = 'Відпочивай'
    return message

def start_command(update: Update, context: CallbackContext):
    message = 'Привіт. Я бот з розкладом твоєї групи.\nДля того щоб продовжити обери номер своєї групи!'
    buttons = [[KeyboardButton('ФІ-12')]]
    users.insert_one({'chat_id':update.effective_chat.id})
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    
def message_handler(update: Update, context: CallbackContext):
    if 'ФІ-12' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-12'}})
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    if 'Тиждень №1' in update.message.text:
        message = 'Вибери день'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'Тиждень №2' in update.message.text:
        message = 'Вибери день'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
    if 'Вибрати тиждень' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    if 'Вибрати групу' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('ФІ-12')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    if 'Понеділок (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Monday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'Вівторок (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Tuesday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'Середа (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Wednesday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'Четвер (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Thursday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'П\'ятниця (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Friday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'Субота (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Saturday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons))
    if 'Понеділок (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Monday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
    if 'Вівторок (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Tuesday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
    if 'Середа (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Wednesday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
    if 'Четвер (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Thursday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
    if 'П\'ятниця (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Friday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
    if 'Субота (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Saturday', 'groups':group})
        message = parse(result_collection)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons))
        
def notification(context: CallbackContext):
    today = datetime.date.today()
    delta = (today - start_date).days
    week = '0'
    if int(delta / 7) % 2 == 0:
        week = '1'
    else:
        week = '2'
    day = today.weekday()
    time = datetime.datetime.now().strftime('%H:%M')
    
    us = users.find()
    print(weekdays[day])
    for user in us:
        result = collection.find({'week':str(week), 'day':weekdays[day], 'time':str(time), 'group':user['group']})
        message = parse(result)
        context.bot.send_message(chat_id=user['chat_id'], text=message)


job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(5,30))
job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(7,25))
job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(9,20))
job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(11,15))
job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(13,10))
job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(15,30))


dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))



updater.start_polling()
updater.idle()
