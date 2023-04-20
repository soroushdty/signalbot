def outer_wrapper(userobject):
    if datetime.datetime.now().timestamp()<=time.mktime(datetime.datetime.strptime(userobject.expire, "%Y/%m/%d").timetuple()):
        logging.info(f'user{userobject.userid} passed datecheck; Expiration date {userobject.expire}.')
        rowlooper(userobject)
        logging.debug(f'user{userobject.userid} fed to rowlooper')
    else:
        logging.info(f'user{userobject.userid} failed datecheck; Expiration date {userobject.expire}.')
        bot = telegram.Bot(token=bottoken)
        bot.send_message(chat_id=f'{userobject.telegramid}signalbot',
        text= f'Your subscription expired at {userobject.expire}, please renew your subscription', timeout=100000)
        logging.debug(f'Telegram message sent to {userobject.telegramid}signalbot')