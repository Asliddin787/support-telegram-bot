from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot token
TOKEN = '6854655697:AAGIDdep6B7n_C20L2_o1qBVFbDFNSMP1Eg'

# /start komandasi uchun funksiya
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Salom, {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

# Oddiy xabarlar uchun funksiya
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Main funksiya
def main() -> None:
    # Updater obyekti va Dispatcher
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # /start komandasi uchun handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Barcha xabarlar uchun handler
    dispatcher.add_handler(MessageHandler(echo))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
