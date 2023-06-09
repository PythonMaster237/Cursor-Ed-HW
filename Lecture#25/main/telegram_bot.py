from telegram import Bot
from django.conf import settings


async def send_telegram_message(message):
    telegram_settings = settings.TELEGRAM
    bot_token = telegram_settings['bot_token']
    channel_name = telegram_settings['channel_name']
    bot = Bot(token=bot_token)
    # await bot.send_message(chat_id="@%s" % channel_name,
    #                  text=message, parse_mode='HTML')
    await bot.send_message(chat_id="@%s" % channel_name,
                     text=message)