import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# GPT-3.5 modelining API kalit so'zini o'rnating
api_key = "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"

# Telegram bot tokenini o'rnating
bot_token = "6001821992:AAFV0-4x-mq8PST8FoKvRv9RkUWWxnBCtkM"

# Telegram chat ID ni o'rnating
chat_id = "489832803"

# OpenAI API-ga ulanish
openai.api_key = api_key
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# ChatGPT dan javob olish uchun funksiya
def get_gpt_response(question):
    response = openai.Completion.create(
        headers=headers,
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1000,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Telegram botga kelgan habarlarga javob berish uchun funksiya
def reply_to_message(update, context):
    message_text = update.message.text
    response = get_gpt_response(message_text)
    context.bot.send_message(chat_id=chat_id, text=response)

# Telegram botni sozlash va ishga tushirish
def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply_to_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()