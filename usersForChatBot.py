from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Foydalanuvchi ID larini saqlash uchun o'zgaruvchilar
user1_id = None
user2_id = None

# /start komandasini bajarganda ishlatiladigan funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Salom! Xush kelibsiz!')

# /register komandasini bajarganda ishlatiladigan funksiya
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global user1_id, user2_id
    user_id = update.message.from_user.id

    if user1_id is None:
        user1_id = user_id
        await update.message.reply_text('Siz birinchi foydalanuvchi sifatida ro\'yxatdan o\'tdingiz.')
    elif user2_id is None:
        user2_id = user_id
        await update.message.reply_text('Siz ikkinchi foydalanuvchi sifatida ro\'yxatdan o\'tdingiz.')
    else:
        await update.message.reply_text('Ikkala foydalanuvchi ham ro\'yxatdan o\'tgan.')

# Xabarni qayta ishlash funksiyasi
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global user1_id, user2_id
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id == user1_id and user2_id is not None:
        await context.bot.send_message(chat_id=user2_id, text=f"Foydalanuvchi 1: {text}")
    elif user_id == user2_id and user1_id is not None:
        await context.bot.send_message(chat_id=user1_id, text=f"Foydalanuvchi 2: {text}")
    else:
        await update.message.reply_text('Ikkala foydalanuvchi ham ro\'yxatdan o\'tishi kerak.')

def main() -> None:
    # Telegram bot tokenini kiritamiz
    application = ApplicationBuilder().token("7360860001:AAFbi5rv064Za5lPDjOTnqfXs7mArRDSRJs").build()

    # /start komandasini boshqarish
    application.add_handler(CommandHandler("start", start))
    # /register komandasini boshqarish
    application.add_handler(CommandHandler("register", register))
    # Xabarlarni boshqarish
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()
