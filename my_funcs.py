import time
import datetime
import telegram
# import ccxt
# import pandas as pd
# import oandapyV20
# import oandapyV20.endpoints.instruments as instruments

###############tokens###############

bottoken = '1337493022:AAFeGpusevfb294e45VEr1LsYD8JesUrAhk'
oandatoken = 'cb95230707ff3a32e562677cf56929d8-256d5fb01977813c733077b1188f896b'

###############datechecker###############

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

###############expired###############
        
    
def rowlooper(DF):
    for row in DF:
        #start a thread of inner wrapper function
def userlooper(userslist):
    for user in userslist:
        #start a thread of outter wrapper function

    
    
    
    
    














#datechecker function

    

#buysell function
def buysell(STP):
    buyselllist =[]
    for x in STP:
       EP = STP[0]
       exchange = EP['Exchange']
       longlist = EP['longpairs']
       shortlist = EP['shortpairs']
       strategy = STP[1]
       tdict = {'Exchange name': exchange ,
                'Buy list': [],
                'Sell list': [],
                'Interval': STP[2]}
       for i in longlist:
           if strategy.pairfilter(i,exchange) and strategy.longfilter(i,exchange):
               tdict['Buy list'].append(i)
       for j in shortlist:
           if strategy.pairfilter(j,exchange) and strategy.shortfilter(j,exchange):
               tdict['Buy list'].append(i)
       buyselllist.append(tdict)
       return buyselllist
       

#duplichecker function
def duplichecker(buyselllist):
    global loopnumber
    loopnumber +=1
    for x in buyselllist:
        pass
        
    


#Enter the expiration date in format of Y/m/d"""
  
  