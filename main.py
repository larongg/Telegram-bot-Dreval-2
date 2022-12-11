import logging
from configs import token, questions, code
# import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ParseMode
from aiogram.utils import executor
import pandas as pd


logging.basicConfig(level=logging.INFO)
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
excel_dreval = {
    'ФИО': [],
    'Группа': [],
    'Результаты': []
}


class User(StatesGroup):
    fio = State()
    group = State()
    test1 = State()
    test2 = State()
    test3 = State()
    test4 = State()
    test5 = State()
    test6 = State()
    test7 = State()
    test8 = State()
    test9 = State()
    test10 = State()
    test11 = State()
    test12 = State()
    test13 = State()
    test14 = State()
    test15 = State()
    test16 = State()
    test17 = State()
    test18 = State()
    test19 = State()
    test20 = State()
    test21 = State()
    test22 = State()
    test23 = State()
    test24 = State()
    test25 = State()
    test26 = State()
    test27 = State()
    test28 = State()
    test29 = State()
    test30 = State()
    test31 = State()
    test32 = State()
    test33 = State()
    test34 = State()
    test35 = State()
    test36 = State()
    test37 = State()
    test38 = State()
    test39 = State()
    test40 = State()
    test41 = State()
    test42 = State()
    test43 = State()
    test44 = State()
    test45 = State()
    test46 = State()
    test47 = State()
    test48 = State()
    test49 = State()
    test50 = State()
    test51 = State()
    test52 = State()
    test53 = State()
    test54 = State()
    test55 = State()
    test56 = State()
    test57 = State()
    test58 = State()
    test59 = State()
    test60 = State()
    test61 = State()
    test62 = State()
    test63 = State()
    test64 = State()
    test65 = State()
    test66 = State()
    test67 = State()
    test68 = State()
    test69 = State()
    test70 = State()
    test71 = State()
    test72 = State()
    test73 = State()
    test74 = State()
    test75 = State()
    test76 = State()
    test77 = State()
    test78 = State()
    test79 = State()
    test80 = State()
    test81 = State()
    test82 = State()
    test83 = State()
    test84 = State()
    test85 = State()
    test86 = State()
    test87 = State()
    test88 = State()
    test89 = State()
    test90 = State()
    test91 = State()
    test92 = State()
    test93 = State()
    test94 = State()
    test95 = State()
    test96 = State()
    test97 = State()
    test98 = State()
    test99 = State()
    test100 = State()
    test101 = State()
    test102 = State()
    test103 = State()
    test104 = State()
    test105 = State()
    test106 = State()
    test107 = State()
    test108 = State()
    test109 = State()
    test110 = State()


@dp.message_handler(commands=code)
async def cmd_excel_print(message: types.Message):
    pd.DataFrame(excel_dreval).to_excel('./dreval.xlsx', index=False)
    await bot.send_document(
        message.chat.id,
        open('dreval.xlsx', 'rb')
    )


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Начало теста
    """
    # Set state
    await User.fio.set()

    await bot.send_message(message.chat.id, "ФИО")


# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=User.fio)
async def process_surname(message: types.Message, state: FSMContext):
    # Update state and data
    async with state.proxy() as data:
        data['fio'] = message.text
    await User.next()

    await bot.send_message(message.chat.id, "Группа")


@dp.message_handler(state=User.group)
async def process_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await User.next()

    # Remove keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Да", "Нет")

    await bot.send_message(
        message.chat.id,
        "Ответь да или нет",
        reply_markup=markup
    )
    await bot.send_message(
        message.chat.id,
        "1: " + questions[0]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test1
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test1)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test1'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "2:" + questions[1]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test2
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test2)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test2'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "3:" + questions[2]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test3
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test3)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test3'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "4:" + questions[3]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test4
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test4)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test4'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "5:" + questions[4]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test5
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test5)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test5'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "6:" + questions[5]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test6
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test6)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test6'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "7:" + questions[6]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test7
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test7)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test7'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "8:" + questions[7]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test8
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test8)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test8'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "9:" + questions[8]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test9
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test9)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test9'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "10:" + questions[9]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test10
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test10)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test10'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "11:" + questions[10]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test11
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test11)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test11'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "12:" + questions[11]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test12
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test12)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test12'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "13:" + questions[12]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test13
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test13)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test13'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "14:" + questions[13]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test14
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test14)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test14'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "15:" + questions[14]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test15
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test15)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test15'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "16:" + questions[15]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test16
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test16)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test16'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "17:" + questions[16]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test17
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test17)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test17'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "18:" + questions[17]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test18
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test18)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test18'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "19:" + questions[18]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test19
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test19)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test19'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "20:" + questions[19]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test20
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test20)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test20'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "21:" + questions[20]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test21
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test21)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test21'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "22:" + questions[21]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test22
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test22)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test22'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "23:" + questions[22]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test23
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test23)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test23'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "24:" + questions[23]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test24
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test24)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test24'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "25:" + questions[24]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test25
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test25)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test25'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "26:" + questions[25]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test26
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test26)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test26'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "27:" + questions[26]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test27
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test27)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test27'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "28:" + questions[27]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test28
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test28)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test28'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "29:" + questions[28]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test29
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test29)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test29'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "30:" + questions[29]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test30
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test30)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test30'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "31:" + questions[30]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test31
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test31)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test31'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "32:" + questions[31]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test32
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test32)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test32'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "33:" + questions[32]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test33
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test33)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test33'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "34:" + questions[33]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test34
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test34)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test34'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "35:" + questions[34]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test35
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test35)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test35'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "36:" + questions[35]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test36
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test36)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test36'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "37:" + questions[36]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test37
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test37)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test37'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "38:" + questions[37]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test38
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test38)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test38'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "39:" + questions[38]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test39
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test39)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test39'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "40:" + questions[39]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test40
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test40)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test40'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "41:" + questions[40]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test41
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test41)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test41'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "42:" + questions[41]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test42
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test42)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test42'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "43:" + questions[42]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test43
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test43)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test43'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "44:" + questions[43]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test44
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test44)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test44'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "45:" + questions[44]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test45
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test45)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test45'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "46:" + questions[45]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test46
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test46)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test46'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "47:" + questions[46]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test47
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test47)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test47'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "48:" + questions[47]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test48
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test48)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test48'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "49:" + questions[48]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test49
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test49)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test49'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "50:" + questions[49]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test50
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test50)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test50'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "51:" + questions[50]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test51
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test51)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test51'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "52:" + questions[51]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test52
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test52)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test52'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "53:" + questions[52]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test53
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test53)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test53'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "54:" + questions[53]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test54
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test54)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test54'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "55:" + questions[54]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test55
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test55)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test55'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "56:" + questions[55]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test56
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test56)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test56'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "57:" + questions[56]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test57
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test57)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test57'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "58:" + questions[57]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test58
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test58)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test58'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "59:" + questions[58]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test59
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test59)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test59'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "60:" + questions[59]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test60
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test60)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test60'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "61:" + questions[60]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test61
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test61)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test61'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "62:" + questions[61]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test62
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test62)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test62'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "63:" + questions[62]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test63
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test63)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test63'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "64:" + questions[63]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test64
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test64)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test64'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "65:" + questions[64]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test65
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test65)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test65'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "66:" + questions[65]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test66
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test66)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test66'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "67:" + questions[66]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test67
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test67)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test67'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "68:" + questions[67]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test68
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test68)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test68'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "69:" + questions[68]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test69
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test69)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test69'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "70:" + questions[69]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test70
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test70)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test70'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "71:" + questions[70]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test71
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test71)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test71'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "72:" + questions[71]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test72
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test72)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test72'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "73:" + questions[72]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test73
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test73)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test73'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "74:" + questions[73]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test74
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test74)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test74'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "75:" + questions[74]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test75
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test75)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test75'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "76:" + questions[75]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test76
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test76)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test76'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "77:" + questions[76]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test77
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test77)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test77'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "78:" + questions[77]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test78
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test78)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test78'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "79:" + questions[78]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test79
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test79)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test79'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "80:" + questions[79]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test80
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test80)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test80'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "81:" + questions[80]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test81
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test81)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test81'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "82:" + questions[81]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test82
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test82)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test82'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "83:" + questions[82]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test83
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test83)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test83'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "84:" + questions[83]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test84
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test84)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test84'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "85:" + questions[84]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test85
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test85)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test85'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "86:" + questions[85]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test86
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test86)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test86'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "87:" + questions[86]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test87
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test87)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test87'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "88:" + questions[87]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test88
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test88)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test88'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "89:" + questions[88]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test89
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test89)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test89'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "90:" + questions[89]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test90
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test90)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test90'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "91:" + questions[90]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test91
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test91)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test91'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "92:" + questions[91]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test92
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test92)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test92'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "93:" + questions[92]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test93
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test93)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test93'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,

        "94:" + questions[93]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test94
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test94)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test94'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,

        "95:" + questions[94]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test95
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test95)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test95'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "96:" + questions[95]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test96
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test96)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test96'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "97:" + questions[96]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test97
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test97)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test97'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "98:" + questions[97]

    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test98
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test98)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test98'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "99:" + questions[98]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test99
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test99)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test99'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "100:" + questions[99]

    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test100
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test100)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test100'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "101:" + questions[100]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test101
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test101)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test101'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,

        "102:" + questions[101]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test102
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test102)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test102'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "103:" + questions[102]

    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test103
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test103)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test103'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "104:" + questions[103]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test104
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test104)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test104'] = message.text
    await User.next()

    await bot.send_message(

        message.chat.id,
        "105:" + questions[104]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test105
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test105)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test105'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "106:" + questions[105]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test106
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test106)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test106'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "107:" + questions[106]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test107
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test107)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test107'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "108:" + questions[107]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test108
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test108)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test108'] = message.text

    await User.next()

    await bot.send_message(
        message.chat.id,
        "109:" + questions[108]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test109
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test109)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test109'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "110:" + questions[109]
    )


@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test110
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test110)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test110'] = message.text

        excel_dreval['ФИО'].append(data['fio'])
        excel_dreval['Группа'].append(data['group'])

        await bot.send_message(
            message.chat.id,
            "CLown",
            reply_markup=types.ReplyKeyboardRemove()
        )

        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
