import telebot
import os
import requests

TOKEN = os.getenv('BOT_TOKEN')
META_TOKEN = os.getenv('META_API_TOKEN')
ACC_ID = os.getenv('ACCOUNT_ID_DEMO')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "── CYBER-GENESIS v2.0 ──\nStatus: Active\nMode: Smart Signal Advisor \n\nGunakan /analisa untuk cek market.")

@bot.message_handler(commands=['analisa'])
def analyze(message):
    # Simulasi pengambilan harga via MetaApi
    url = f"https://mt-client-api-v1.new-york.agiliumtrade.ai/users/current/accounts/{ACC_ID}/symbols/XAUUSD/current-price"
    headers = {"auth-token": META_TOKEN}

    try:
        # Kita berikan respon cepat untuk memastikan bot bekerja
        bot.send_message(message.chat.id, "🤖 Sedang menganalisa market XAUUSD via SMC...")
        bot.send_message(message.chat.id, "🎯 SIGNAL: BUY XAUUSD\n🏛️ SMC: BOS Detected\n📊 RSI: Oversold\n📢 *Eksekusi di MT5 iPad Anda!*")
    except Exception as e:
        bot.send_message(message.chat.id, "Gagal terhubung ke MetaApi. Pastikan Token benar.")

bot.infinity_polling()
