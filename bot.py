
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != OWNER_ID:
        await update.message.reply_text("هذا البوت خاص بصاحبه فقط.")
        return

    await update.message.reply_text(
        "مرحباً بك في بوت حجز الوجبات الجامعية 🍽️\n\n"
        "البوت يعمل بنجاح.\n"
        "المطعم: مطعم مركزي\n"
        "الوجبات: الفطور والغداء والعشاء\n\n"
        "استخدم /status لمعرفة حالة النظام."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != OWNER_ID:
        return

    await update.message.reply_text(
        "🟢 بوت Telegram يعمل.\n"
        "🔴 لم يتم ربط WebEtu بعد.\n"
        "🔴 لم يتم تنفيذ أي حجز."
    )


def main():
    if not TOKEN or not OWNER_ID:
        raise RuntimeError("إعداد TELEGRAM_BOT_TOKEN و OWNER_ID مطلوب.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
