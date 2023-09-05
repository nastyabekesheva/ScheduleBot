from telegram.ext import *
from telegram import *
import pymongo
from pymongo import MongoClient
from typing import Union, List
import pytz
import os

import datetime
import logging

MONGO_URL = os.environ['MONGO_URL']
TOKEN = os.environ['TOKEN']

cluster = MongoClient(m)
db = cluster['ScheduleDB']
collection = db['schedule']
users = db['users']
suggestions = db['suggestions']

start_date = datetime.date(2022, 9, 5)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

defaults = Defaults(parse_mode=ParseMode.HTML, tzinfo=pytz.timezone('Europe/Kyiv'))
updater = Updater(token=TOKEN, use_context=True, defaults=defaults)

dispatcher = updater.dispatcher
j = updater.job_queue
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

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

def build_menu(
    buttons: List[InlineKeyboardButton],
    n_cols: int,
    header_buttons: Union[InlineKeyboardButton, List[InlineKeyboardButton]]=None,
    footer_buttons: Union[InlineKeyboardButton, List[InlineKeyboardButton]]=None
) -> List[List[InlineKeyboardButton]]:
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons if isinstance(header_buttons, list) else [header_buttons])
    if footer_buttons:
        menu.append(footer_buttons if isinstance(footer_buttons, list) else [footer_buttons])
    return menu

def start_command(update: Update, context: CallbackContext):
    message = 'Привіт. Я бот з розкладом твоєї групи.\nДля того щоб продовжити обери номер своєї групи!'
    button_list = [
        InlineKeyboardButton("ФІ-31", callback_data='fi-31'),
        InlineKeyboardButton("ФІ-33", callback_data='fi-33'),
        InlineKeyboardButton("ФІ-21", callback_data='fi-21'),
        InlineKeyboardButton("ФІ-23", callback_data='fi-23'),
        InlineKeyboardButton("ФІ-11", callback_data='fi-11'),
        InlineKeyboardButton("ФІ-12", callback_data='fi-12'),
        InlineKeyboardButton("ФІ-02", callback_data='fi-02'),
        InlineKeyboardButton("ФІ-03", callback_data='fi-03')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=4))
    if users.find({'chat_id':update.effective_chat.id}) != '':
        users.insert_one({'chat_id':update.effective_chat.id, 'username':update.effective_chat.username, 'elected':[], 'group':'', 'notify':True})
    else:
        users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'elected':[], 'group':''}})
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = reply_markup)

def restart_command(update: Update, context: CallbackContext):
    message = 'Вибери групу!'
    button_list = [
        InlineKeyboardButton("ФІ-31", callback_data='fi-31'),
        InlineKeyboardButton("ФІ-33", callback_data='fi-33'),
        InlineKeyboardButton("ФІ-21", callback_data='fi-21'),
        InlineKeyboardButton("ФІ-23", callback_data='fi-23'),
        InlineKeyboardButton("ФІ-11", callback_data='fi-11'),
        InlineKeyboardButton("ФІ-12", callback_data='fi-12'),
        InlineKeyboardButton("ФІ-02", callback_data='fi-02'),
        InlineKeyboardButton("ФІ-03", callback_data='fi-03')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=4))
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'elected':[], 'group':''}})
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = reply_markup)

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
    buttons.append([KeyboardButton('Завершити')])
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
    buttons.append([KeyboardButton('Завершити')])
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
    
def select_week_command(update: Update, context: CallbackContext):
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрери тиждень:"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup = reply_markup)

def fi_31(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-31'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-31"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_33(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-33'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-33"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_21(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-21'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-21"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_23(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-23'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-23"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_11(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-11'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-11"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_12(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-12'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-12"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_02(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-02'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-02"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def fi_03(update: Update, context: CallbackContext):
    users.update_one({'chat_id':update.effective_chat.id}, {'$set':{'group':'fi-03'}})
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрано групу: ФІ-03"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def week_1(update: Update, context: CallbackContext):
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    message = "Вибрано перший тиждень"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def week_2(update: Update, context: CallbackContext):
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    message = "Вибрано другий тиждень"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def select_group(update: Update, context: CallbackContext):
    button_list = [
        InlineKeyboardButton("ФІ-31", callback_data='fi-31'),
        InlineKeyboardButton("ФІ-33", callback_data='fi-33'),
        InlineKeyboardButton("ФІ-21", callback_data='fi-21'),
        InlineKeyboardButton("ФІ-23", callback_data='fi-23'),
        InlineKeyboardButton("ФІ-11", callback_data='fi-11'),
        InlineKeyboardButton("ФІ-12", callback_data='fi-12'),
        InlineKeyboardButton("ФІ-02", callback_data='fi-02'),
        InlineKeyboardButton("ФІ-03", callback_data='fi-03')
    ]
    message = "Вибери групу"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=4))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)

def select_week(update: Update, context: CallbackContext):
    button_list = [
        InlineKeyboardButton("Тиждень №1", callback_data='week_1'),
        InlineKeyboardButton("Тиждень №2", callback_data='week_2'),
        InlineKeyboardButton("Вибрати групу", callback_data='select_group')
    ]
    message = "Вибрери тиждень:"
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup)
    
def monday_1(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'1', 'day':'Monday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def tuesday_1(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'1', 'day':'Tuesday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def wednesday_1(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'1', 'day':'Wednesday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def thursday_1(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'1', 'day':'Thursday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def friday_1(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'1', 'day':'Friday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def saturday_1(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'1', 'day':'Saturday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_1'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_1'),
        InlineKeyboardButton("Середа", callback_data='wednesday_1'),
        InlineKeyboardButton("Четвер", callback_data='thursday_1'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_1'),
        InlineKeyboardButton("Субота", callback_data='saturday_1'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
        
def monday_2(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'2', 'day':'Monday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def tuesday_2(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'2', 'day':'Tuesday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def wednesday_2(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'2', 'day':'Wednesday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def thursday_2(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'2', 'day':'Thursday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def friday_2(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'2', 'day':'Friday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)
    
def saturday_2(update: Update, context: CallbackContext):
    user = users.find({'chat_id':update.effective_chat.id})
    group = user[0]['group']
    result_collection = collection.find({'week':'2', 'day':'Saturday', 'groups':group})
    message = parse(result_collection, update.effective_chat.id)
    button_list = [
        InlineKeyboardButton("Понеділок", callback_data='monday_2'),
        InlineKeyboardButton("Вівторок", callback_data='tuesday_2'),
        InlineKeyboardButton("Середа", callback_data='wednesday_2'),
        InlineKeyboardButton("Четвер", callback_data='thursday_2'),
        InlineKeyboardButton("П'ятниця", callback_data='friday_2'),
        InlineKeyboardButton("Субота", callback_data='saturday_2'),
        InlineKeyboardButton("Вибрати тиждень", callback_data='select_week')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message, reply_markup = reply_markup, parse_mode=ParseMode.HTML)



def message_handler(update: Update, context: CallbackContext):
    subjects = get_elected_subjects(update.effective_chat.id)
    
    if 'Завершити' in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Вибір завершено', reply_markup=ReplyKeyboardRemove())

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
    t = datetime.datetime.now(pytz.timezone('Europe/Kyiv')) + datetime.timedelta(minutes=5)
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
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(8,25))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(10,20))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(12,15))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(14,10))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(16,5))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(18,25))
    job_daily = j.run_daily(notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(13,55))
    job_daily = j.run_daily(morning_notification, days=(0, 1, 2, 3, 4, 5), time=datetime.time(7,59))



    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('restart', restart_command))
    dispatcher.add_handler(CommandHandler('select', select_command))
    dispatcher.add_handler(CommandHandler('unselect', unselect_command))
    dispatcher.add_handler(CommandHandler('suggest', suggest_command))
    dispatcher.add_handler(CommandHandler('end', end_command))
    dispatcher.add_handler(CommandHandler('addtochannel', addtochannel_command))
    dispatcher.add_handler(CommandHandler('notify', notify_command))
    dispatcher.add_handler(CommandHandler('stopnotify', stop_notify_command))
    dispatcher.add_handler(CommandHandler('selectweek', select_week_command))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_31, pattern='fi-31'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_33, pattern='fi-33'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_21, pattern='fi-21'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_23, pattern='fi-23'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_11, pattern='fi-11'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_12, pattern='fi-12'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_02, pattern='fi-02'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fi_03, pattern='fi-03'))
    updater.dispatcher.add_handler(CallbackQueryHandler(week_1, pattern='week_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(week_2, pattern='week_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(select_group, pattern='select_group'))
    updater.dispatcher.add_handler(CallbackQueryHandler(select_week, pattern='select_week'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monday_1, pattern='monday_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tuesday_1, pattern='tuesday_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(wednesday_1, pattern='wednesday_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(thursday_1, pattern='thursday_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(friday_1, pattern='friday_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(saturday_1, pattern='saturday_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monday_2, pattern='monday_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tuesday_2, pattern='tuesday_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(wednesday_2, pattern='wednesday_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(thursday_2, pattern='thursday_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(friday_2, pattern='friday_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(saturday_2, pattern='saturday_2'))
    
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
