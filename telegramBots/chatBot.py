import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging sozlamalari
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start komandasini qabul qilish uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Salom! Men Telegram botman. Sizga qanday yordam bera olaman?')

# Oddiy xabarlarni qabul qilish uchun funksiya
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Xatoliklarni qayd qilish uchun funksiya
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

# Botni boshlash funksiyasi
def main() -> None:
    # Bot tokeningizni bu yerga kiriting
    token = '7360860001:AAFbi5rv064Za5lPDjOTnqfXs7mArRDSRJs'

    # Application obyekti yaratamiz
    application = Application.builder().token(token).build()

    # /start komandasini qabul qilish uchun handler qo'shamiz
    application.add_handler(CommandHandler("start", start))

    # Oddiy xabarlarni qabul qilish uchun handler qo'shamiz
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Xatoliklarni qayd qilish uchun handler qo'shamiz
    application.add_error_handler(error)

    # Botni ishga tushiramiz
    application.run_polling()

if __name__ == '__main__':
    main()
