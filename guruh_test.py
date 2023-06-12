import logging
from aiogram import Bot, Dispatcher, types

API_TOKEN = '5847287723:AAENWGI7Wh3s2tkKFs6H_el2FxA4dTg1_-U'
GROUP_CHAT_ID = 626573623

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Botni o'rnatish va Dispatcherni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Guruhdagi xabarlarga javob berish
@dp.message_handler(content_types=types.ContentTypes.TEXT, func=lambda message: message.chat.id == GROUP_CHAT_ID)
async def reply_to_group_message(message: types.Message):
    massag = message.text.lower()
    print(massag)
    # Xabar bilan bot logikasini bajarish
    # Masalan:
    await message.reply('Salom! Men guruhdagi habarlarga javob beraman.')


# Telegram botni ishga tushirish
if __name__ == '__main__':
    dp.run_polling()