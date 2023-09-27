# author: https://github.com/vmzhivetyev/tg-vnstat-monitor-bot.git

import asyncio
import os
import logging

from telegram import Update, InputMediaPhoto
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
)

from vnstat import vnstat_this_month_usage, human_bytes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


TOKEN = os.environ.get("TOKEN")
#LIMIT_GIB = 1024 ** 3 * int(os.environ.get("LIMIT_GIB"))
#LIMIT_GIB = 0
INTERFACE = os.environ.get("INTERFACE")
TG_CHAT_ID = os.environ.get("TG_CHAT_ID")


async def start(update: Update, context: CallbackContext):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"I'm a bot, please talk to me! Your id: {update.effective_chat.id}"
    )


async def status(update: Update, context: CallbackContext):
    await send_status(update.effective_chat.id)


async def send_status(chat_id):
    interface_name, rx, tx, total, month = vnstat_this_month_usage(interface_name=INTERFACE)
    path =  '/home/mohammad/monitoring/'
    text = f'''Usage on {interface_name} in {month}:
⬇️ rx {human_bytes(rx)}
⬆️ tx {human_bytes(tx)}
Total: {human_bytes(total)}
'''
    files = [file for file in ['vnstat.png', 'ports.png'] if os.path.exists(path+file) ]

    if len(files) > 1:
        await application.bot.send_media_group(
            chat_id=chat_id,
                caption=text,
                media=[InputMediaPhoto(open(file, 'rb')) for file in files])
    elif len(files) == 1:
        await application.bot.send_photo(TG_CHAT_ID, caption=text, photo=open(files[0], 'rb'))
    else:
        await application.bot.send_message(chat_id=chat_id, text=text)


if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('status', status))

    asyncio.get_event_loop().run_until_complete(send_status(chat_id=TG_CHAT_ID))

    #application.run_polling()
