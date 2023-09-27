from aiogram import Bot, Dispatcher, types, executor
from config import token
import random
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def get_random(message:types.Message):
    await message.reply("Я загадал число от 1 до 3 угадайте")

@dp.message_handler()
async def get_answer(message:types.Message):
    number = random.randint(1,3)
    user_input = int(message.text)
    if user_input == number:
        await message.reply("Вы угадали")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    elif user_input > 3:
        await message.reply("Пишите только цифры до 3")
    else:
        await message.reply(f"Ууупс вы не угадали! Это было число: {number}")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")


executor.start_polling(dp)
