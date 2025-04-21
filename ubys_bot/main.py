from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import mesage_control
import threading
import manager  # manager.py içindeki fonksiyonu çağıracağız

BOT_TOKEN = "your bot token"
manager_thread = None

def start_manager_if_not_running():
    global manager_thread
    if manager_thread is None or not manager_thread.is_alive():
        manager_thread = threading.Thread(target=manager.run_manager_loop, daemon=True)
        manager_thread.start()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    chat_id = update.message.chat.id

    if "start" in text:
        mesage_control.set_active(True)
        start_manager_if_not_running()
        await context.bot.send_message(chat_id=chat_id, text="✅ Bot aktif edildi. Veri çekimi başladı.")
    elif "stop" in text:
        mesage_control.set_active(False)
        await context.bot.send_message(chat_id=chat_id, text="⛔ Bot durduruldu. Veri çekimi durduruldu.")
    else:
        await context.bot.send_message(chat_id=chat_id, text="Komut tanınmadı. 'start' veya 'stop' yazabilirsin.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Telegram bot dinlemede...")
    app.run_polling()
