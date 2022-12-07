with open('run.txt', 'w') as f:
    for i in range(120):
        f.write(
            """\n\n@dp.message_handler(
    lambda message: message.text not in ['Да', 'Нет'],
    state=User.test{0}
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Ответь да или нет"
    )


@dp.message_handler(state=User.test{1})
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test{2}'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "{3}:" + questions[{4}]
    )""".format(i,i,i,i+1,i)
        )
