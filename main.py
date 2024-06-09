from auth_data import token
import requests
from datetime import datetime
import telebot
from telebot import types

def crypto_bahalar(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    jogaby = requests.get(url)
    data=jogaby.json()

    shu_gun_senesi = datetime.now().strftime("%d.%m.%Y %H:%M")

    if crypto in data and "usd" in data[crypto]:
        return f" {crypto.capitalize()} bahasy: {data[crypto]['usd']}$\nSene: {shu_gun_senesi}"
    else:
        return "Bagyslan kriptowalyutan bahasyny bilmedim"
    
    
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_knopka(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btc_knopca = types.InlineKeyboardButton("Bitcoin bahasy", callback_data="bitcoin")
    ltc_knopca = types.InlineKeyboardButton("Litecoin bahasy", callback_data="litecoin")
    eth_knopca = types.InlineKeyboardButton("Ethreum bahasy", callback_data="ethereum")

    keyboard.add(btc_knopca, ltc_knopca, eth_knopca)

    bot.send_message(message.chat.id, "Haysy kriptowalyutan bahasyny bilesiniz gelyar?", reply_markup=keyboard)    

@bot.callback_query_handler(func= lambda call:True)
def knopca_basylynda_jogap(callback):
    if callback.message:
        bahasy = crypto_bahalar(callback.data)
        bot.send_message(callback.message.chat.id, bahasy)
        start_knopka(callback.message)
        
bot.polling()