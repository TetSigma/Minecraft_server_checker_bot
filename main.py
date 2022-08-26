from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from mcstatus import JavaServer
import asyncio

TOKEN = "put_your_token"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer('\n /checker - checks if server is online, sends notifications if not  \n /status - current server state')


#Sends current server state when asked
@dp.message_handler(commands=['status'])
async def command_status(message: types.Message):
    try:
      # Put your server IP here
      server = JavaServer("your_server_ip")
      status = server.status()
      await message.answer(f"Server is online! \n  {status.players.online} are online \n Ping = {status.latency} ms")
    except:
        await message.answer('Server is broken!')

#Starts checking server state, sends message if server is broken
@dp.message_handler(commands=['checker'])
async def command_checker(message: types.Message):
    while True:
        await asyncio.sleep(600) #Put check time in seconds here 
        try:
            server = JavaServer("your_server_ip")
            status = server.status()
            # Enable this code to send notifications when server is online
            #await message.answer_animation('https://media3.giphy.com/media/xT0GqgeTVaAdWZD1uw/giphy.gif')
            #await message.answer("Server Status - Online")
        except:
            #Enable this code to send walter white gif every time when server is broken
            #await message.answer_animation('https://media3.giphy.com/media/xT0GqgeTVaAdWZD1uw/giphy.gif')
            await message.answer("Server is broken")


executor.start_polling(dp, skip_updates=True)
