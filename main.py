from config import TOKEN
from errorhandler import error
from commands import start_command, help_command, info_command
from processchat import handle_message, process_file, process_image
from telegram.ext import Application, CommandHandler, MessageHandler, filters


if __name__ == '__main__':
    print('Bot started...')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('info', info_command))
    app.add_handler(MessageHandler(filters.PHOTO, process_image))
    app.add_handler(MessageHandler(filters.Document.PDF, process_file))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print('Bot polling...')
    app.run_polling(poll_interval=3)