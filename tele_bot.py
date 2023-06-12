"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import openai
import time 

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6001821992:AAFV0-4x-mq8PST8FoKvRv9RkUWWxnBCtkM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Salom!\nChat GPT ga hush kelibsiz.")

@dp.message_handler()
async def echo(message: types.Message):
    massag=message.text.lower()

    api_key = "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"

    # OpenAI API-ga ulanish
    openai.api_key = api_key
    
    question = massag
    time.sleep(5)
    # ChatGPT ga so'rov yuborish
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=question,
        max_tokens=1000,  # Javobda maksimal belgi soni
        n=1,  # Nechta javob variantini qaytarish (faqat 1 ta)
        stop=None,  # Javobni to'xtatish uchun so'zl# Foaydalanmoqchi bo'lgn model (masalan, "text-davinci-003")arni kiritish (masalan, "Qiziqarli bo'lmang", "Yana bir savolim bor", ...)
    )
    print(response)
    time.sleep(5)

    # Javobni olish
    answer = response.choices[0].text.strip()
    
    await message.answer(f"Javob:\n {answer}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
