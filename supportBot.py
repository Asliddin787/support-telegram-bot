import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Bot tokeningizni kiriting
TOKEN = '7360860001:AAFbi5rv064Za5lPDjOTnqfXs7mArRDSRJs'
ADMIN_CHAT_ID = '1070907281'  # Adminning Telegram chat ID sini kiriting

# /start komandasini aniqlash
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    await update.message.reply_text(f'Salom, {user.first_name}! Sizning xabaringizni qabul qildim.')

# Foydalanuvchi xabarlarini qabul qilish va adminlarga yuborish
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    user_message = update.message.text

    # Adminlarga xabarni yuborish
    admin_message = f"Yangi xabar:\n\nFrom: {user.username} ({user.id})\nMessage: {user_message}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)

    # Foydalanuvchiga javob
    await update.message.reply_text('Rahmat! Sizning xabaringiz adminlarga yuborildi.')

# Adminlarning foydalanuvchilarga javob qaytarishi uchun handler
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if str(update.message.chat_id) != ADMIN_CHAT_ID:
        return  # Agar bu admin bo'lmasa, qaytib chiqish

    try:
        # Admindan yuborilgan xabar formati: /reply <user_id> <message>
        args = context.args
        if len(args) < 2:
            await update.message.reply_text('Foydalanuvchiga javob berish uchun: /reply <user_id> <message>')
            return

        user_id = args[0]
        reply_message = ' '.join(args[1:])

        # Foydalanuvchiga javob yuborish
        await context.bot.send_message(chat_id=user_id, text=reply_message)
        await update.message.reply_text('Foydalanuvchiga javob yuborildi.')
    except Exception as e:
        await update.message.reply_text(f'Xatolik yuz berdi: {e}')

def main() -> None:
    # Loglarni sozlash
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # ApplicationBuilder va botni yaratish
    application = ApplicationBuilder().token(TOKEN).build()

    # /start komandasini aniqlash
    application.add_handler(CommandHandler("start", start))

    # Foydalanuvchi xabarlarini qabul qilish uchun handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Adminning foydalanuvchilarga javob qaytarishi uchun /reply komandasi
    application.add_handler(CommandHandler("reply", reply))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()
