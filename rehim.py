
#pyrogram

from pyrogram import Client, filters



api_id = "15954332"
api_hash = "85adea6f1eaf068b707703b4846a9ced"
bot_token = "5953314004:AAGBOQREULge79JT9WGq4MalrD2DQFb_78c"



rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)


@rehim.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")
			
    
#TELETHON SETRİ



rehim.run()

