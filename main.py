import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


tg_bot_token = '5056900362:AAH49O-wx1GURCX85LZM5KIoRO2Tmh8rv0g'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

all_data_list = []
page = 1
main_request = requests.get(f'https://rickandmortyapi.com/api/character?page={page}')
all_data = main_request.json()
characters_raw = all_data['results']
next_page_url = all_data['info']['next']
prev_page_url = all_data['info']['prev']
characters = {}
characters_names = []


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global characters_names

    characters_names = []
    for value in characters_raw:
        characters_names.append(value['name'])

    inline_btn_1 = InlineKeyboardButton(characters_names[0], callback_data='1')
    inline_btn_2 = InlineKeyboardButton(characters_names[1], callback_data='2')
    inline_btn_3 = InlineKeyboardButton(characters_names[2], callback_data='3')
    inline_btn_4 = InlineKeyboardButton(characters_names[3], callback_data='4')
    inline_btn_5 = InlineKeyboardButton(characters_names[4], callback_data='5')
    inline_btn_6 = InlineKeyboardButton(characters_names[5], callback_data='6')
    inline_btn_7 = InlineKeyboardButton(characters_names[6], callback_data='7')
    inline_btn_8 = InlineKeyboardButton(characters_names[7], callback_data='8')
    inline_btn_9 = InlineKeyboardButton(characters_names[8], callback_data='9')
    inline_btn_10 = InlineKeyboardButton(characters_names[9], callback_data='10')
    inline_btn_11 = InlineKeyboardButton(characters_names[10], callback_data='11')
    inline_btn_12 = InlineKeyboardButton(characters_names[11], callback_data='12')
    inline_btn_13 = InlineKeyboardButton(characters_names[12], callback_data='13')
    inline_btn_14 = InlineKeyboardButton(characters_names[13], callback_data='14')
    inline_btn_15 = InlineKeyboardButton(characters_names[14], callback_data='15')
    inline_btn_16 = InlineKeyboardButton(characters_names[15], callback_data='16')
    inline_btn_17 = InlineKeyboardButton(characters_names[16], callback_data='17')
    inline_btn_18 = InlineKeyboardButton(characters_names[17], callback_data='18')
    inline_btn_19 = InlineKeyboardButton(characters_names[18], callback_data='19')
    inline_btn_20 = InlineKeyboardButton(characters_names[19], callback_data='20')
    inline_btn_21 = InlineKeyboardButton("Prev page", callback_data='prev')
    inline_btn_22 = InlineKeyboardButton("Next page", callback_data='next')

    inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4,
                                                           inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8,
                                                           inline_btn_9
                                                           , inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13,
                                                           inline_btn_14, inline_btn_15, inline_btn_16, inline_btn_17
                                                           , inline_btn_18, inline_btn_19, inline_btn_20, inline_btn_21
                                                           , inline_btn_22)
    await message.answer("Бот Рик и Морти", reply_markup=inline_kb_full)

@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    global characters, characters_names, main_request, next_page_url, prev_page_url, all_data, characters_raw, page

    for values in characters_raw:
        characters[values['id']] = values     # Сортировка по ид

    code = callback_query.data
    if code not in ['next', 'prev']:
        if page > 1:
            code = int(code) + ((page - 1) * 20)
        elif page == 1:
            code = code
        else:
            print("Error")
        print(code)
        character = characters.get(int(code))
        caption = (f"""
                ID: {character['id']}
                Имя: {character['name']}
                Пол: {character['gender']}
                Раса: {character['species']}
                """)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=character['image'], caption=caption)
    elif code == 'next':
        try:
            page += 1
            main_request = requests.get(f'{next_page_url}')
            all_data = main_request.json()
            characters_raw = all_data['results']
            next_page_url = all_data['info']['next']
            prev_page_url = all_data['info']['prev']
            characters_names = []
            for value in characters_raw:
                characters_names.append(value['name'])
            if page == 42:
                inline_btn_1 = InlineKeyboardButton(characters_names[0], callback_data='1')
                inline_btn_2 = InlineKeyboardButton(characters_names[1], callback_data='2')
                inline_btn_3 = InlineKeyboardButton(characters_names[2], callback_data='3')
                inline_btn_4 = InlineKeyboardButton(characters_names[3], callback_data='4')
                inline_btn_5 = InlineKeyboardButton(characters_names[4], callback_data='5')
                inline_btn_6 = InlineKeyboardButton(characters_names[5], callback_data='6')
                inline_btn_7 = InlineKeyboardButton("Prev page", callback_data='prev')
                inline_btn_8 = InlineKeyboardButton("Next page", callback_data='next')
                inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2, inline_btn_3,
                                                                       inline_btn_4,
                                                                       inline_btn_5, inline_btn_6, inline_btn_7,
                                                                       inline_btn_8)
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text='================================================',
                                       reply_markup=inline_kb_full)
            else:
                inline_btn_1 = InlineKeyboardButton(characters_names[0], callback_data='1')
                inline_btn_2 = InlineKeyboardButton(characters_names[1], callback_data='2')
                inline_btn_3 = InlineKeyboardButton(characters_names[2], callback_data='3')
                inline_btn_4 = InlineKeyboardButton(characters_names[3], callback_data='4')
                inline_btn_5 = InlineKeyboardButton(characters_names[4], callback_data='5')
                inline_btn_6 = InlineKeyboardButton(characters_names[5], callback_data='6')
                inline_btn_7 = InlineKeyboardButton(characters_names[6], callback_data='7')
                inline_btn_8 = InlineKeyboardButton(characters_names[7], callback_data='8')
                inline_btn_9 = InlineKeyboardButton(characters_names[8], callback_data='9')
                inline_btn_10 = InlineKeyboardButton(characters_names[9], callback_data='10')
                inline_btn_11 = InlineKeyboardButton(characters_names[10], callback_data='11')
                inline_btn_12 = InlineKeyboardButton(characters_names[11], callback_data='12')
                inline_btn_13 = InlineKeyboardButton(characters_names[12], callback_data='13')
                inline_btn_14 = InlineKeyboardButton(characters_names[13], callback_data='14')
                inline_btn_15 = InlineKeyboardButton(characters_names[14], callback_data='15')
                inline_btn_16 = InlineKeyboardButton(characters_names[15], callback_data='16')
                inline_btn_17 = InlineKeyboardButton(characters_names[16], callback_data='17')
                inline_btn_18 = InlineKeyboardButton(characters_names[17], callback_data='18')
                inline_btn_19 = InlineKeyboardButton(characters_names[18], callback_data='19')
                inline_btn_20 = InlineKeyboardButton(characters_names[19], callback_data='20')
                inline_btn_21 = InlineKeyboardButton("Prev page", callback_data='prev')
                inline_btn_22 = InlineKeyboardButton("Next page", callback_data='next')

                inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2, inline_btn_3,
                                                                       inline_btn_4,
                                                                       inline_btn_5, inline_btn_6, inline_btn_7,
                                                                       inline_btn_8,
                                                                       inline_btn_9
                                                                       , inline_btn_10, inline_btn_11, inline_btn_12,
                                                                       inline_btn_13,
                                                                       inline_btn_14, inline_btn_15, inline_btn_16,
                                                                       inline_btn_17
                                                                       , inline_btn_18, inline_btn_19, inline_btn_20,
                                                                       inline_btn_21
                                                                       , inline_btn_22)
                await bot.send_message(chat_id=callback_query.from_user.id, text='================================================', reply_markup=inline_kb_full)
        except:
            await bot.send_message(chat_id=callback_query.from_user.id, text='Max level')
    elif code == 'prev':
        try:
            main_request = requests.get(f'{prev_page_url}')
            all_data = main_request.json()
            characters_raw = all_data['results']
            next_page_url = all_data['info']['next']
            prev_page_url = all_data['info']['prev']
            page -= 1
            characters_names = []
            for value in characters_raw:
                characters_names.append(value['name'])

            inline_btn_1 = InlineKeyboardButton(characters_names[0], callback_data='1')
            inline_btn_2 = InlineKeyboardButton(characters_names[1], callback_data='2')
            inline_btn_3 = InlineKeyboardButton(characters_names[2], callback_data='3')
            inline_btn_4 = InlineKeyboardButton(characters_names[3], callback_data='4')
            inline_btn_5 = InlineKeyboardButton(characters_names[4], callback_data='5')
            inline_btn_6 = InlineKeyboardButton(characters_names[5], callback_data='6')
            inline_btn_7 = InlineKeyboardButton(characters_names[6], callback_data='7')
            inline_btn_8 = InlineKeyboardButton(characters_names[7], callback_data='8')
            inline_btn_9 = InlineKeyboardButton(characters_names[8], callback_data='9')
            inline_btn_10 = InlineKeyboardButton(characters_names[9], callback_data='10')
            inline_btn_11 = InlineKeyboardButton(characters_names[10], callback_data='11')
            inline_btn_12 = InlineKeyboardButton(characters_names[11], callback_data='12')
            inline_btn_13 = InlineKeyboardButton(characters_names[12], callback_data='13')
            inline_btn_14 = InlineKeyboardButton(characters_names[13], callback_data='14')
            inline_btn_15 = InlineKeyboardButton(characters_names[14], callback_data='15')
            inline_btn_16 = InlineKeyboardButton(characters_names[15], callback_data='16')
            inline_btn_17 = InlineKeyboardButton(characters_names[16], callback_data='17')
            inline_btn_18 = InlineKeyboardButton(characters_names[17], callback_data='18')
            inline_btn_19 = InlineKeyboardButton(characters_names[18], callback_data='19')
            inline_btn_20 = InlineKeyboardButton(characters_names[19], callback_data='20')
            inline_btn_21 = InlineKeyboardButton("Prev page", callback_data='prev')
            inline_btn_22 = InlineKeyboardButton("Next page", callback_data='next')

            inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2, inline_btn_3,
                                                                   inline_btn_4,
                                                                   inline_btn_5, inline_btn_6, inline_btn_7,
                                                                   inline_btn_8,
                                                                   inline_btn_9
                                                                   , inline_btn_10, inline_btn_11, inline_btn_12,
                                                                   inline_btn_13,
                                                                   inline_btn_14, inline_btn_15, inline_btn_16,
                                                                   inline_btn_17
                                                                   , inline_btn_18, inline_btn_19, inline_btn_20,
                                                                   inline_btn_21
                                                                   , inline_btn_22)
            await bot.send_message(chat_id=callback_query.from_user.id, text='================================================', reply_markup=inline_kb_full)
        except:
            await bot.send_message(chat_id=callback_query.from_user.id, text='Min level')
executor.start_polling(dp)
