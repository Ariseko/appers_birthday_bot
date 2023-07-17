from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenuKeyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Все об апперах',
                                                                              callback_data='aboutUppers'),
                                                         InlineKeyboardButton(text='20 июля: Празднуем вместе',
                                                                              callback_data='20July'),
                                                         InlineKeyboardButton(text='Викторина про апперов',
                                                                              callback_data='quiz'),
                                                         InlineKeyboardButton(text='Конкурс детского рисунка',
                                                                              callback_data='competition'))

backToMainMenu = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='В главное меню',
                                                                            callback_data='backToMainMenu'))

julyEventKeyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Да, буду очно в московском ШК 🎂',
                                                                               callback_data='ochno'),
                                                          InlineKeyboardButton(text='Да, буду по Zoom 🎉',
                                                                               callback_data='zoom'),
                                                          InlineKeyboardButton(text='К сожалению, не смогу 😔',
                                                                               callback_data='cant'))

isQuizStarting = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Да, поехали!',
                                                                            callback_data='start'),
                                                       InlineKeyboardButton(text='Пока нет',
                                                                            callback_data='nope'))

q1Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. Базя',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Пинг',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. Пуш',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. Юнг',
                                                                        callback_data='Г'))

q2Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. Соты',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Аппы',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. Юнги',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. Бази',
                                                                        callback_data='Г'))

q3Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. Пинг',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Пуш',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. Юнг',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. Никто',
                                                                        callback_data='Г'))

q4Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. 10%',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. 20%',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. 30%',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. 50%',
                                                                        callback_data='Г'))

q5Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. Пуш',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Пинг',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. Юнг',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. Базя',
                                                                        callback_data='Г'))

q6Keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. 1 день',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. 7 дней',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. 30 дней',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. 365 дней',
                                                                        callback_data='Г'))

q7Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. Пинг',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Пуш',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. Тапа',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. Базя',
                                                                        callback_data='Г'))

q8Keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. С молодежью',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Со старшим поколением',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. С мигрантами',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. С семейными клиентами',
                                                                        callback_data='Г'))

q9Keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='А. Пинг',
                                                                        callback_data='А'),
                                                   InlineKeyboardButton(text='Б. Пуш',
                                                                        callback_data='Б'),
                                                   InlineKeyboardButton(text='В. Базя',
                                                                        callback_data='В'),
                                                   InlineKeyboardButton(text='Г. Тапа',
                                                                        callback_data='Г'))

q10Keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Дискотека Авария',
                                                                         callback_data='А'),
                                                    InlineKeyboardButton(text='Б. Иванушки Int',
                                                                         callback_data='Б'),
                                                    InlineKeyboardButton(text='В. Стрелки',
                                                                         callback_data='В'),
                                                    InlineKeyboardButton(text='Г. Ария',
                                                                         callback_data='Г'))
