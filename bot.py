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
suggestions = db['suggestions']

start_date = datetime.date(2022, 9, 5)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

updater = Updater(token='5651742670:AAE3IU3a99mn92IM_6Xz-hMPIfLSSgRI1Fc', use_context=True)
dispatcher = updater.dispatcher
j = updater.job_queue
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

week_1_buttons = [[KeyboardButton('Понеділок (т. 1)'), KeyboardButton('Вівторок (т. 1)')], [KeyboardButton('Середа (т. 1)'), KeyboardButton('Четвер (т. 1)')], [KeyboardButton('П\'ятниця (т. 1)'), KeyboardButton('Субота (т. 1)')], [KeyboardButton('Вибрати тиждень')]]
week_2_buttons = [[KeyboardButton('Понеділок (т. 2)'), KeyboardButton('Вівторок (т. 2)')], [KeyboardButton('Середа (т. 2)'), KeyboardButton('Четвер (т. 2)')], [KeyboardButton('П\'ятниця (т. 2)'), KeyboardButton('Субота (т. 2)')], [KeyboardButton('Вибрати тиждень')]]

def bold(
    text,
    trans=str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
        "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵",
    ),
):
    return text.translate(trans)

def parse(result_collection, id):

    new_result = []
    for r in result_collection:
        if r['elective'] == False:
            new_result.append(r)
        elif r['elective'] == True:
            user = users.find({'chat_id':id})
            if user[0]['elected']:
                if r['name'] in user[0]['elected']:
                    new_result.append(r)
            else:
                new_result.append(r)
    
    messages = {}
    
    message = ''
    for r in new_result:
        if r['time'] == '08:30':
            try:
                messages[1].append(f'1\uFE0F\u20E3 пара (08:30)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({1 : [f'1\uFE0F\u20E3 пара (08:30)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
                
        if r['time'] == '10:25':
            try:
                messages[2].append(f'2\uFE0F\u20E3 пара (10:25)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({2 : [f'2\uFE0F\u20E3 пара (10:25)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
        if r['time'] == '12:20':
            try:
                messages[3].append(f'3\uFE0F\u20E3 пара (12:20)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({3 : [f'3\uFE0F\u20E3 пара (12:20)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
        if r['time'] == '14:15':
            try:
                messages[4].append(f'4\uFE0F\u20E3 пара (14:15)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({4 : [f'4\uFE0F\u20E3 пара (14:15)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
        if r['time'] == '16:10':
            try:
                messages[5].append(f'5\uFE0F\u20E3 пара (16:10)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({5 : [f'5\uFE0F\u20E3 пара (16:10)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
        if r['time'] == '18:30':
            try:
                messages[6].append(f'6\uFE0F\u20E3 пара (18:30)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({6 : [f'6\uFE0F\u20E3 пара (18:30)\n{r["name"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
    
    messages = dict(sorted(messages.items()))
    for i in messages:
        temp = ''.join(messages[i])
        message += temp
    if message == '':
        message = 'Відпочивай'
    return message

def get_elected_subjects(id):
    user = users.find({'chat_id':id})
    group = user[0]['group']
    subjects = collection.find({'groups':group, 'elective':True})
    subjects_names = []
    for subject in subjects:
        subjects_names.append(subject['name'])
    subjects_names = sorted(list(set(subjects_names)))
    
    return subjects_names

def start_command(update: Update, context: CallbackContext):
    message = 'Привіт. Я бот з розкладом твоєї групи.\nДля того щоб продовжити обери номер своєї групи!'
    buttons = [[KeyboardButton('ФІ-12')]]
    users.insert_one({'chat_id':update.effective_chat.id, 'elected':[], 'group':''})
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    
    
def select_command(update: Update, context: CallbackContext):
    message = 'Вибери предмет за номером:\n'
    subjects_names = get_elected_subjects(update.effective_chat.id)
    buttons = []
    user = users.find({'chat_id':update.effective_chat.id})
    for i in range(len(subjects_names)):
        if subjects_names[i] not in user[0]['elected']:
            message += f'{i} - {subjects_names[i]}\n'
            buttons.append([KeyboardButton(f'{i}')])
    buttons.append([KeyboardButton('Вибрати тиждень')])
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    
def unselect_command(update: Update, context: CallbackContext):
    message = 'Вибери предмет за номером:\n'
    subjects_names = get_elected_subjects(update.effective_chat.id)
    buttons = []
    user = users.find({'chat_id':update.effective_chat.id})
    for i in range(len(subjects_names)):
        if subjects_names[i] in user[0]['elected']:
            message += f'{i} - {subjects_names[i]}\n'
            buttons.append([KeyboardButton(f'{i}')])
    #users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'elected':[]}})
    buttons.append([KeyboardButton('Вибрати тиждень')])
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    
def suggest_command(update: Update, context: CallbackContext):
    suggestions.insert_one({'chat_id':update.effective_chat.id, 'username':update.effective_chat.username, 'message':update.message.text})
    context.bot.send_message(chat_id=update.effective_chat.id, text='Відгук відправлено')
    
    
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
        message = 'Вибери групу'
        buttons = [[KeyboardButton('ФІ-12')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    if 'Понеділок (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Monday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons), parse_mode=ParseMode.HTML)
    if 'Вівторок (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Tuesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons), parse_mode=ParseMode.HTML)
    if 'Середа (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Wednesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons), parse_mode=ParseMode.HTML)
    if 'Четвер (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Thursday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons), parse_mode=ParseMode.HTML)
    if 'П\'ятниця (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Friday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons), parse_mode=ParseMode.HTML)
    if 'Субота (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Saturday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons), parse_mode=ParseMode.HTML)
    if 'Понеділок (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Monday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons), parse_mode=ParseMode.HTML)
    if 'Вівторок (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Tuesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons), parse_mode=ParseMode.HTML)
    if 'Середа (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Wednesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons), parse_mode=ParseMode.HTML)
    if 'Четвер (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Thursday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons), parse_mode=ParseMode.HTML)
    if 'П\'ятниця (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Friday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons), parse_mode=ParseMode.HTML)
    if 'Субота (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Saturday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons), parse_mode=ParseMode.HTML)
    subjects = get_elected_subjects(update.effective_chat.id)
    for i in range(len(subjects)):
        if str(i) == update.message.text:
            if subjects[i] not in users.find({'chat_id':update.effective_chat.id})[0]['elected']:
                users.update_one({'chat_id':update.effective_chat.id}, {'$push':{'elected':subjects[i]}})
            else:
                users.update_one({'chat_id':update.effective_chat.id}, {'$pull':{'elected':subjects[i]}})
        
def notification(context: CallbackContext):
    today = datetime.date.today()
    delta = (today - start_date).days
    week = '0'
    if int(delta / 7) % 2 == 0:
        week = '1'
    else:
        week = '2'
    day = today.weekday()
    t = datetime.datetime.now()+ datetime.timedelta(hours=3)
    t = t.time()
    j = t.strftime('%H:%M')

    
    us = users.find()
    for user in us:
        result = collection.find({'week':week, 'day':weekdays[day],  'groups':user['group']})
        temp = []
        for i in result:
            if i['time']==t.strftime('%H:%M'):
                temp.append(i)
        message = parse(temp, user['chat_id'])
        if message != 'Відпочивай':
            context.bot.send_message(chat_id=user['chat_id'], text=message, parse_mode=ParseMode.HTML)
        
def morning_notification(context: CallbackContext):
    today = datetime.date.today()
    delta = (today - start_date).days
    start_message = f'{today} - День {delta+1}\n\n'
    week = '0'
    if int(delta / 7) % 2 == 0:
        week = '1'
    else:
        week = '2'
    day = today.weekday()
    us = users.find()
    for user in us:
        result = collection.find({'week':week, 'day':weekdays[day],  'groups':user['group']})
        message = parse(result, user['chat_id'])
        if message != 'Відпочивай':
            context.bot.send_message(chat_id=user['chat_id'], text=bold(start_message)+message, parse_mode=ParseMode.HTML)
    

def main():
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(5,30))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(7,25))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(9,20))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(11,15))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(13,10))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(15,30))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(15,50))
    job_daily = j.run_daily(morning_notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(9,46))

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('select', select_command))
    dispatcher.add_handler(CommandHandler('unselect', unselect_command))
    dispatcher.add_handler(CommandHandler('suggest', suggest_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

#'time':t.strftime('%H:%M'),
