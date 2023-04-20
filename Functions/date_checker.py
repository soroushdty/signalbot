def datechecker(userobject):
    d=datetime.datetime.strptime(userobject.expiration, '%Y/%m/%d')
    today=datetime.datetime.today()
    if d>=today:
        return True
    else:
        bot = telegram.Bot(token=bottoken)
        bot.send_message(chat_id=f'{userobject.telegramid}_scanner',
        text=f'Your {userobject.subscription} subscription expired at {userobject.expiration}. Contact us for renewal.', timeout=100000)
        print(f'User{userobject.userid} subscription expired at {userobject.expiration}.')
        return False
    

#alt
def datechecker(userobject):
    expire = userobject.expire
    userid = userobject.userid
    telegramid = userobject.telegramid
    if datetime.datetime.now().timestamp()>time.mktime(datetime.datetime.strptime(expire, "%Y/%m/%d").timetuple()):
        #Log: {username}, user {userid}   Subscription expired at {expiration date}
        bot = telegram.Bot(token=bottoken)
        bot.send_message(chat_id=f'@{telegramid}signalbot',
        text= f'Your subscription expired at{expire},please renew your subscription', timeout=100000)
        return False
    else:
        return True    