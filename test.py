'''@dp.message_handler(
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
        "{0}: " + questions[106]
    )'''.f