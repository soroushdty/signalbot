###############wrapper###############
def wrapper(userid,row,telegramid):
    while True:
        now = datetime.datetime.now(tz=tz)
        if row['List Name']:
            print(f'START user{userid}*{row["Exchange"]}*{row["List Name"]}*{row["Strategy"].strategyname}*{now.strftime("%d %b %H:%M:%S")}')
        else:
            print(f'START user{userid}*{row["Exchange"]}*{row["Strategy"].strategyname}*{now.strftime("%d %b %H:%M:%S")}')
        s1=signalmaker(row)
        s2=stringmaker(s1)
        s3=telesender(s2, telegramid)
        now = datetime.datetime.now(tz=tz)
        if row['List Name']:
            print(f'COMPLETE user{userid}*{row["List Name"]}*{row["Exchange"]}*{row["Strategy"].strategyname}*{now.strftime("%d %b %H:%M:%S")}')
        else:
            print(f'COMPLETE user{userid}*{row["Exchange"]}*{row["Strategy"].strategyname}*{now.strftime("%d %b %H:%M:%S")}')
        time.sleep(row['Strategy'].loop)



#outer_wrapper
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


#inner wrapper
def inner_wrapper(row,strategyclass,telegramid):
    logging.info('signalmaker started')
    s1=signalmaker(row,strategyclass)
    logging.info('duplichecker started')
    s2=duplichecker(s1)
    logging.info('stringmaker started')
    s3=stringmaker(s2)
    logging.info('telesender started')
    telesender(s3,telegramid)
    logging.info('All finished; Going into sleep mode')
    time.sleep(strategyclass.timer)


#Wrapper Function
def wrapper():
  s1 = buysell(long_list,short_list,EMACross)
  s2 = duplichecker(s1)
  s3 = stringmaker(s2)
  telemessager(s3)