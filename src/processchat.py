from config.config import BOT_USER
from handler.handler import handle_file, handle_resp
from telegram import Update # type: ignore
from telegram.ext import ContextTypes # type: ignore

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    response = None

    if message_type in ("group", "supergroup"):
        if BOT_USER in text:
            new_text: str = text.replace(BOT_USER, '').strip()
            response = handle_resp(new_text)

    elif message_type == "private":
        response = handle_resp(text)

    if response:
        print(f'Bot: {response}')
        await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')

async def process_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    #await file.download_to_drive()
    flink = file.file_path
    resptext: str = handle_file(flink)
    await update.message.reply_text(resptext)
   # await update.message.reply_text(handle_file)

async def process_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.document.file_id
    file = await context.bot.get_file(file_id)
    #await file.download_to_drive()
    flink = file.file_path
    # print(flink)
    resptext: str = handle_file(flink)
    await update.message.reply_text(resptext)