import os
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset di Railway Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

LINK_ALTERNATIF = "https://cutt.ly/GtFHqLcQ"
GROUP_WHATSAPP = "https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C"
LIVE_CHAT = "https://direct.lc.chat/19758862"
DAFTAR_SEKARANG = LINK_ALTERNATIF


WELCOME_TEXT = """PARISBOLA OFFICIAL

Selamat datang di layanan resmi Parisbola!

Transaksi deposit QRIS proses hanya 1 detik
Penarikan berapapun dibayar tuntas tanpa ribet
Sistem cepat, stabil dan pelayanan terbaik

Link Alternatif: https://cutt.ly/GtFHqLcQ
Group WhatsApp:
https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C
Live Chat 24 Jam: https://direct.lc.chat/19758862

Akses sekarang dan rasakan pengalaman terbaik bersama
PARISBOLA!"""


def menu_buttons():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Link Alternatif", url=LINK_ALTERNATIF),
        InlineKeyboardButton("Group WhatsApp", url=GROUP_WHATSAPP),
        InlineKeyboardButton("Live Chat 24 Jam", url=LIVE_CHAT),
        InlineKeyboardButton("Daftar Sekarang", url=DAFTAR_SEKARANG),
    )
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=menu_buttons(),
        disable_web_page_preview=True,
    )


@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=menu_buttons(),
        disable_web_page_preview=True,
    )


if __name__ == "__main__":
    logging.info("Bot Parisbola berjalan...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)
