from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime
from keyboards import *
from answersText import *
from questionsText import *

import json
import requests
import sqlite3 as sq

hookURL = 'https://hook.eu1.make.com/wdnwoajce7fgkhylo8wiu6sznxo5kc3u'

base = sq.connect('check.db')
cursor = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE)')
base.commit()


class StatesClass(StatesGroup):
    getRealName = State()
    explanation = State()
    julyEventState = State()

    quizStartState = State()
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    quizEnding = State()


storage = MemoryStorage()
bot = Bot(token='6299354069:AAFS1PCkHrWmTD3GH58e2dfKU1PeoMQdUxY')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    photo = open('static/hello.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo,
                         caption=f'Давай знакомиться! Мы – <b>Базя, Пинг, Юнг, Тапа и Пуш</b>. Мы живем во всем, '
                                 f'что делает наша '
                                 f'компания, но в первую очередь – в мобильном приложении билайна. \n\nА как тебя '
                                 f'зовут?\n\n<i>Укажи свои имя и фамилию</i>',
                         parse_mode='html')
    await StatesClass.getRealName.set()


@dp.message_handler(state=StatesClass.getRealName)
async def receivingRealName(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['RealName'] = message.text
        data['telegramUsername'] = message.from_user.mention

    await message.answer('Супер! А теперь расскажем, что тебя ждет в эту праздничную неделю. '
                         'Спойлер: будет мноооого интересного!\n'
                         '• Викторина с призами\n'
                         '• Интервью с каждым из нас\n'
                         '• Конкурс детского рисунка\n'
                         '• <b>Праздничное ток-шоу и игра в честь нашего дня рождения!</b>\n\n'
                         'Просто выбери, о чем ты хочешь узнать в первую очередь:', parse_mode='html')

    await message.answer('С чего начнем?', reply_markup=mainMenuKeyboard)

    await StatesClass.explanation.set()


@dp.callback_query_handler(state=StatesClass.explanation)
async def distribution(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'aboutUppers':
        photo = open('static/uppers.jpg', 'rb')
        await bot.send_photo(callback.from_user.id, photo=photo,
                             caption=f'Наконец-то мы познакомимся поближе! Скорее заходи на <a '
                                     f'href="https://space.beeline.ru/Regions/retailbusiness/Pages/uppers_hb.aspx'
                                     f'">праздничную страницу</a>🎉'
                                     f'\n\nКаждый день на ней будет появляться интервью с одним из нас. Честно '
                                     f'говоря, у нас впервые берут интервью, поэтому мы немного стесняемся. Поделись '
                                     f'потом впечатлениями, ладно?',
                             parse_mode='html',
                             reply_markup=mainMenuKeyboard)
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)

    elif callback.data == '20July':
        photo = open('static/20july.jpg', 'rb')
        await bot.send_photo(callback.from_user.id, photo=photo,
                             caption=f'Ух ты, настоящий день рождения!\nПразднуем 20 июля, ты приглашен!\nВ программе '
                                     f'– целый фильм про нас, ток-шоу с представителями команды апперов и прикольная '
                                     f'игра в прямом эфире. Ты придешь?',
                             parse_mode='html',
                             reply_markup=julyEventKeyboard)
        await StatesClass.julyEventState.set()
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)

    elif callback.data == 'competition':
        photo = open('static/drawing.jpg', 'rb')
        await bot.send_photo(callback.from_user.id, photo=photo,
                             caption=f'Мы тоже любим приятные слова и подарочки, особенно сделанные своими руками. '
                                     f'Поэтому объявили самый милый творческий конкурс для юных билайновцев. \n<b>Работы '
                                     f'принимаются до 23 июля!</b>\nВсе подробности ты найдешь <a '
                                     f'href="https://space.beeline.ru/Regions/retailbusiness/Pages/uppers_pics.aspx'
                                     f'">на этой странице.</a>\nОтмечаем вместе!',
                             parse_mode='html',
                             reply_markup=mainMenuKeyboard)
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)

    elif callback.data == 'quiz':
        photo = open('static/quiz.jpg', 'rb')

        await bot.send_photo(callback.from_user.id, photo=photo,
                             caption=f'Мы знаем, как ты любишь соревноваться с коллегами и получать подарки. Самое '
                                     f'время проверить свои силы и знания!\n<b>20 участников</b>, ответивших на все '
                                     f'вопросы правильно и быстрее всех, станут обладателями небольшой приятности от '
                                     f'нас! <b>Играем до 23 июля включительно!</b>\n\nНачинаем?',
                             parse_mode='html',
                             reply_markup=isQuizStarting)
        await StatesClass.quizStartState.set()
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)


@dp.callback_query_handler(state=StatesClass.julyEventState)
async def julyEvent(callback: types.CallbackQuery):
    if callback.data == 'ochno':
        await bot.send_message(callback.from_user.id,
                               text=f'<a href="https://wheretogo.beeline.ru/hbd_uppers_shk/">Ссылка на '
                                    f'регистрацию</a> 🧐', parse_mode='html', reply_markup=mainMenuKeyboard)
        await StatesClass.explanation.set()
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)
    elif callback.data == 'zoom':
        await bot.send_message(callback.from_user.id,
                               text=f'<a href="https://wheretogo.beeline.ru/hbd_uppers_zoom/">Ссылка на '
                                    f'регистрацию</a> 🧐', parse_mode='html', reply_markup=mainMenuKeyboard)
        await StatesClass.explanation.set()
        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)
    else:
        await bot.send_message(callback.from_user.id,
                               text=f'Жаль 🥺\nЧем еще займёмся?', parse_mode='html', reply_markup=mainMenuKeyboard)
        await StatesClass.explanation.set()

        await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                            reply_markup=None)


@dp.callback_query_handler(state=StatesClass.quizStartState)
async def quizStarts(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'start':
        photo = open('static/q1.jpg', 'rb')
        await bot.send_photo(callback.from_user.id, photo=photo,
                             caption=q1Question,
                             parse_mode='html',
                             reply_markup=q1Keyboard)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        async with state.proxy() as data:
            data['quizTimeStart'] = f'{dt_string}'
        await StatesClass.q1.set()

    elif callback.data == 'nope':
        await bot.send_message(callback.from_user.id, text="Тогда пока можешь почитать про другие наши активности 😉",
                               reply_markup=mainMenuKeyboard)
        await StatesClass.explanation.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q1)
async def q1Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'Б':
        async with state.proxy() as data:
            data['counter'] = 1

    photo = open('static/q2.jpg', 'rb')
    photoRobot = open('static/ping1.png', 'rb')

    await bot.send_photo(callback.from_user.id, photo=photoRobot,caption=q1Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q2Question,
                         reply_markup=q2Keyboard)
    await StatesClass.q2.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q2)
async def q2Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'А':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q3.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q2Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q3Question,
                         reply_markup=q3Keyboard)
    await StatesClass.q3.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q3)
async def q3Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'В':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q4.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q3Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q4Question,
                         reply_markup=q4Keyboard)
    await StatesClass.q4.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q4)
async def q4Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'Б':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q5.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q4Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q5Question,
                         reply_markup=q5Keyboard)
    await StatesClass.q5.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q5)
async def q5Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'Г':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q6.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q5Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q6Question,
                         reply_markup=q6Keyboard)
    await StatesClass.q6.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q6)
async def q6Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'В':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q7.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q6Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q7Question,
                         reply_markup=q7Keyboard)
    await StatesClass.q7.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q7)
async def q7Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'В':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q8.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q7Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q8Question,
                         reply_markup=q8Keyboard)
    await StatesClass.q8.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q8)
async def q8Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'Г':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q9.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q8Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q9Question,
                         reply_markup=q9Keyboard)
    await StatesClass.q9.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q9)
async def q9Func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'Б':
        async with state.proxy() as data:
            data['counter'] += 1

    photo = open('static/q10.jpg', 'rb')
    await bot.send_message(callback.from_user.id, text=q9Answer)
    await bot.send_photo(callback.from_user.id, photo=photo,
                         caption=q10Question,
                         reply_markup=q10Keyboard)
    await StatesClass.q10.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


@dp.callback_query_handler(state=StatesClass.q10)
async def q10Func(callback: types.CallbackQuery, state: FSMContext):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    async with state.proxy() as data:
        if callback.data == 'А':
            data['counter'] += 1
        dataToSend = {
            "quizTimeStart": f"{data['quizTimeStart']}",
            "quizTimeEnd": f"{dt_string}",
            "telegramUsername": f"{callback.from_user.mention}",
            "RealName": f"{data['RealName']}",
            "rightAnswers": f"{data['counter']}"
        }
        name = cursor.execute(f'SELECT username from users where username = "{callback.from_user.mention}"').fetchone()
        if name is None:
            cursor.execute(f'INSERT INTO users VALUES ("{callback.from_user.mention}")')
            base.commit()
            r = requests.post(hookURL, data=json.dumps(dataToSend), headers={'Content-Type': 'application/json'})
    print(dataToSend)

    photo = open('static/upperNewYear.jpg', 'rb')
    await bot.send_photo(callback.from_user.id, photo=photo, caption=q10Answer)
    await bot.send_message(callback.from_user.id, text="Ууух, это было здорово!\n\nРезультаты игры будут известны 25 "
                                                       "июля! А пока можешь почитать про другие наши активности",
                           reply_markup=mainMenuKeyboard)

    await StatesClass.explanation.set()
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                        reply_markup=None)


executor.start_polling(dp, skip_updates=True)
