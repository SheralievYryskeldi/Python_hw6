from aiogram import types, Dispatcher
from bot_instance import dp, bot
from parser import tv_show

async def parser_anime(message: types.Message):
    data = tv_show.parser()
    for z in data:
        await bot.send_message(message.chat.id, z)
    # await bot.send_message(message.chat.id, data)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(parser_anime, commands=['parse'])