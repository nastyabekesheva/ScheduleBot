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
            for u in user:
                if u['elected']:
                    if r['name'] in u['elected']:
                        new_result.append(r)
                else:
                    new_result.append(r)
    
    new_result = [i for n, i in enumerate(new_result) if i not in new_result[n + 1:]]
        
    messages = {}
    
    message = ''
    for r in new_result:
        print(r)
        if r['time'] == '08:30':
            try:
                messages[1].append(f'1\uFE0F\u20E3 пара (08:30)\n{r["name"]}\n\U0001f4dc {r["type"]} \n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({1 : [f'1\uFE0F\u20E3 пара (08:30)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
            for i in range(len(messages[1])):
                if 'Кохтич' in messages[1][i]:
                    messages[1][i] = messages[1][i].replace('\U0001f9d1\U0001f3fb\u200D\U0001f3eb', '\u267F')
                
        if r['time'] == '10:25':
            try:
                messages[2].append(f'2\uFE0F\u20E3 пара (10:25)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({2 : [f'2\uFE0F\u20E3 пара (10:25)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
            for i in range(len(messages[2])):
                if 'Кохтич' in messages[2][i]:
                    messages[2][i] = messages[2][i].replace('\U0001f9d1\U0001f3fb\u200D\U0001f3eb', '\u267F')
                    
        if r['time'] == '12:20':
            try:
                messages[3].append(f'3\uFE0F\u20E3 пара (12:20)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({3 : [f'3\uFE0F\u20E3 пара (12:20)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
            for i in range(len(messages[3])):
                if 'Кохтич' in messages[3][i]:
                    messages[3][i] = messages[3][i].replace('\U0001f9d1\U0001f3fb\u200D\U0001f3eb', '\u267F')
                    
        if r['time'] == '14:15':
            try:
                messages[4].append(f'4\uFE0F\u20E3 пара (14:15)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({4 : [f'4\uFE0F\u20E3 пара (14:15)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
            for i in range(len(messages[4])):
                if 'Кохтич' in messages[4][i]:
                    messages[4][i] = messages[4][i].replace('\U0001f9d1\U0001f3fb\u200D\U0001f3eb', '\u267F')
                    
        if r['time'] == '16:10':
            try:
                messages[5].append(f'5\uFE0F\u20E3 пара (16:10)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({5 : [f'5\uFE0F\u20E3 пара (16:10)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
            for i in range(len(messages[5])):
                if 'Кохтич' in messages[5][i]:
                    messages[5][i] = messages[5][i].replace('\U0001f9d1\U0001f3fb\u200D\U0001f3eb', '\u267F')
                    
        if r['time'] == '18:30':
            try:
                messages[6].append(f'6\uFE0F\u20E3 пара (18:30)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n')
            except KeyError:
                messages.update({6 : [f'6\uFE0F\u20E3 пара (18:30)\n{r["name"]}\n\U0001f4dc {r["type"]}\n\U0001f9d1\U0001f3fb\u200D\U0001f3eb {r["teacher"]}\nПосилання: <a href="{r["link"]}">тут</a>\n\n']})
            for i in range(len(messages[6])):
                if 'Кохтич' in messages[6][i]:
                    messages[6][i] = messages[6][i].replace('\U0001f9d1\U0001f3fb\u200D\U0001f3eb', '\u267F')
                    
    
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
    buttons = [[KeyboardButton('ФІ-23')], [KeyboardButton('ФІ-11')], [KeyboardButton('ФІ-12')], [KeyboardButton('ФІ-02')], [KeyboardButton('ФІ-03')]]
    users.insert_one({'chat_id':update.effective_chat.id, 'username':update.effective_chat.username, 'elected':[], 'group':'', 'notify':True})
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))

def restart_command(update: Update, context: CallbackContext):
    message = 'Вибери групу!'
    buttons = [[KeyboardButton('ФІ-23')], [KeyboardButton('ФІ-11')], [KeyboardButton('ФІ-12')], [KeyboardButton('ФІ-02')], [KeyboardButton('ФІ-03')]]
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'elected':[], 'group':''}})
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons))
    
def end_command(update: Update, context: CallbackContext):
    message = 'Допобачення'
    buttons = []
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
    
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
    
def addtochannel_command(update: Update, context: CallbackContext):
    message = 'Для того щоб додати бота до каналу напиши мені повідомлення у виглядіЖ\n \'Додати до каналу {тег або id каналу} {номер групи} \' без лапок({})\n групу писати у вигляді : fi-75 '
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def notify_command(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'notify':True}})
    context.bot.send_message(chat_id=update.effective_chat.id, text='Сповіщення увімкнено!', reply_markup = ReplyKeyboardMarkup([]))
def stop_notify_command(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'notify':False}})
    context.bot.send_message(chat_id=update.effective_chat.id, text='Сповіщення вимкнено!', reply_markup = ReplyKeyboardMarkup([]))
    
def message_handler(update: Update, context: CallbackContext):
    if 'ФІ-23' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-23'}})
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'ФІ-12' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-12'}})
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'ФІ-03' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-03'}})
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'ФІ-02' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-02'}})
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'ФІ-11' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-11'}})
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'Тиждень №1' in update.message.text:
        message = 'Вибери день'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_1_buttons, one_time_keyboard=True))
    if 'Тиждень №2' in update.message.text:
        message = 'Вибери день'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(week_2_buttons, one_time_keyboard=True))
    if 'Вибрати тиждень' in update.message.text:
        message = 'Вибери тиждень'
        buttons = [[KeyboardButton('Тиждень №1')], [KeyboardButton('Тиждень №2')], [KeyboardButton('Вибрати групу')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'Вибрати групу' in update.message.text:
        message = 'Вибери групу'
        buttons = [[KeyboardButton('ФІ-23')], [KeyboardButton('ФІ-11')], [KeyboardButton('ФІ-12')], [KeyboardButton('ФІ-02')],  [KeyboardButton('ФІ-03')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    if 'Понеділок (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Monday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Вівторок (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Tuesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Середа (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Wednesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Четвер (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Thursday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'П\'ятниця (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Friday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Субота (т. 1)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'1', 'day':'Saturday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Понеділок (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Monday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Вівторок (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Tuesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Середа (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Wednesday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Четвер (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Thursday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'П\'ятниця (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Friday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    if 'Субота (т. 2)' in update.message.text:

        user = users.find({'chat_id':update.effective_chat.id})
        group = user[0]['group']
        result_collection = collection.find({'week':'2', 'day':'Saturday', 'groups':group})
        message = parse(result_collection, update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)
    subjects = get_elected_subjects(update.effective_chat.id)
    
    if 'Додати до каналу' in update.message.text:
        message = update.message.text.split()
        try:
            id = message[3]
            group = message[4]
            users.insert_one({'chat_id':id, 'group':group, 'elected':[]})
            context.bot.send_message(chat_id=update.effective_chat.id, text='Успіх!')
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Невірний формат повідомлення', parse_mode=ParseMode.HTML)
        
    
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
    t = datetime.datetime.now()+ datetime.timedelta(hours=3,minutes=5)
    t = t.time()
    j = t.strftime('%H:%M')

    
    us = users.find({'notify':True})
    for user in us:
        result = collection.find({'week':week, 'day':weekdays[day],  'groups':user['group']})
        temp = []
        for i in result:
            if i['time']==t.strftime('%H:%M'):
                temp.append(i)
        message = parse(temp, user['chat_id'])
        if message != 'Відпочивай':
            try:
                context.bot.send_message(chat_id=user['chat_id'], text=message, parse_mode=ParseMode.HTML)
            except Exception as e:
                print(e)
            except TelegramError as te:
                print(te)
            except Unauthorized as ue:
                print(ue)
            
        
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
    us = users.find({'notify':True})
    for user in us:
        result = collection.find({'week':week, 'day':weekdays[day],  'groups':user['group']})
        message = parse(result, user['chat_id'])
        if message != 'Відпочивай':
            try:
                context.bot.send_message(chat_id=user['chat_id'], text=bold(start_message)+message, parse_mode=ParseMode.HTML)
            except Exception as e:
                print(e)
            except TelegramError as te:
                print(te)
            except Unauthorized as ue:
                print(ue)
    

def main():
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(6,25))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(8,20))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(10,15))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(11,10))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(14,5))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(16,25))
    job_daily = j.run_daily(morning_notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(5,59))
    
    

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('restart', restart_command))
    dispatcher.add_handler(CommandHandler('select', select_command))
    dispatcher.add_handler(CommandHandler('unselect', unselect_command))
    dispatcher.add_handler(CommandHandler('suggest', suggest_command))
    dispatcher.add_handler(CommandHandler('end', end_command))
    dispatcher.add_handler(CommandHandler('addtochannel', addtochannel_command))
    dispatcher.add_handler(CommandHandler('notify', notify_command))
    dispatcher.add_handler(CommandHandler('stopnotify', stop_notify_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    

