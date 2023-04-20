def telesender(final_string,telegramid):
    if final_string !=None:
        bot = telegram.Bot(token=bottoken)
        bot.send_message(chat_id=telegramid, text= final_string, timeout=100000) 