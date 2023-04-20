def telesender(final_string,telegramid):
    if final_string !=None:
        bot = telegram.Bot(token=bottoken)
        bot.send_message(chat_id=telegramid, text= final_string, timeout=100000)


#Telegram Function
def telemessager(signalstring):
  if signalstring != None:
    bot = telegram.Bot(token=bottoken)
    bot.send_message(chat_id=chatid, text= signalstring, timeout=100000)