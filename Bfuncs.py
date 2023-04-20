###############imports###############
import telegram
import time
import datetime
import pytz
import pandas as pd
import ccxt
import sys
import threading
###############tokens###############
bottoken='1083677633:AAH5PJnu8-ufqwGQwZvB3oW70fLeMKtCwz8'
oandatoken = 'cb95230707ff3a32e562677cf56929d8-256d5fb01977813c733077b1188f896b'
###############timezone###############
tz=pytz.timezone('Asia/Tehran')
###############datechecker###############
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
    
###############signalmaker###############
def signalmaker(row):
  buy = []
  sell = []
  exchange=row['Exchange']
  listname=row['List Name']
  longs=row['Longs']
  shorts=row['Shorts']
  strategy=row['Strategy']
  for x in longs:
       try:
           if strategy.filtercriteria(exchange,x) and strategy.longcriteria(exchange,x):
               buy.append(x)
       except:
           e = sys.exc_info()[0]
           if listname:
               print(f'FAIL {exchange}*{listname}*{strategy.strategyname}*{x}*{e}')
           else:
               print(f'FAIL {exchange}*{strategy.strategyname}*{x}*{e}')
  for x in shorts:
       try:
           if strategy.filtercriteria(exchange,x) and strategy.shortcriteria(exchange,x):
               sell.append(x)
       except:
           e = sys.exc_info()[0]
           if listname:
               print(f'FAIL {exchange}*{listname}*{strategy.strategyname}*{x}*{e}')
           else:
               print(f'FAIL {exchange}*{strategy.strategyname}*{x}*{e}')
  signaldict={'Exchange':exchange, 'List Name':listname, 'Strategy':strategy.strategyname,
            'Buy':buy, 'Sell':sell}
  return signaldict
###############stringmaker###############
def stringmaker(signaldict):
    finalstring=''
    exchange=signaldict['Exchange']
    listname=signaldict['List Name']
    strategyname=signaldict['Strategy']
    
    buy =''
    if signaldict['Buy']:
        for x in signaldict['Buy']:
            buy='\n'+x+buy
    
    sell=''
    if signaldict['Sell']:
        for x in signaldict['Sell']:
            sell='\n'+x+sell
    
    if listname:
        if buy and sell:
            finalstring ="""
    ***
    Exchange: {}
    List Name: {}
    Strategy: {}
    Buys:{}
    Sells:{}
    ***
    """.format(exchange, listname, strategyname,buy,sell)
        elif buy and not sell:
            finalstring ="""
    ***
    Exchange: {}
    List Name: {}
    Strategy: {}
    Buys:{}
    ***
    """.format(exchange, listname, strategyname,buy)
        elif sell and not buy:
            finalstring ="""
    ***
    Exchange: {}
    List Name: {}
    Strategy: {}
    Sells:{}
    ***
    """.format(exchange,listname, strategyname,sell)
    else:
        if buy and sell:
            finalstring ="""
    ***
    Exchange: {}
    Strategy: {}
    Buys:{}
    Sells:{}
    ***
    """.format(exchange,strategyname,buy,sell)
        elif buy and not sell:
            finalstring ="""
    ***
    Exchange: {}
    Strategy: {}
    Buys:{}
    ***
    """.format(exchange,strategyname,buy)
        elif sell and not buy:
            finalstring ="""
    ***
    Exchange: {}
    Strategy: {}
    Sells:{}
    ***
    """.format(exchange,strategyname,sell)
    
    if finalstring:
        return finalstring
    else:
        return None
    
###############telesender###############
def telesender(finalstring,telegramid):
  if finalstring:
    bot = telegram.Bot(token=bottoken)
    bot.send_message(chat_id=f'{telegramid}_scanner', text=finalstring, timeout=100000)

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
        
###############threader###############
def threader(userobject):
    pairs=userobject.pairs
    userid=userobject.userid
    telegramid = userobject.telegramid
    s0 = datechecker(userobject)
    if s0:
        if type(pairs) == pd.DataFrame:
            for i in range(len(pairs.index)):
                t = threading.Thread(target=wrapper,args=(userid,pairs.iloc[i],telegramid))
                t.start()                    
        elif type(pairs) == pd.Series:
            wrapper(userid,pairs,telegramid)
    
####################ohlcgrabber####################
def ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates,p={}):
  unit = timeframe[-1]
  multiplier = timeframe[:-1]
  ohlc_dict = {                                                                                                             
'Open':'first',                                                                                                    
'High':'max',                                                                                                       
'Low':'min',                                                                                                        
'Close': 'last',                                                                                                    
'Volume': 'sum'}
  if timeframe in rates:
    kline = pd.DataFrame(exchangeinstance.fetchOHLCV(symbol,timeframe,limit=limit,params=p))
    kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    kline.set_index('Time',inplace=True, drop=True)
    kline.index = pd.to_datetime(kline.index,unit='ms')
    return kline  
  else:
    if unit.lower() == 'm':
        kline = pd.DataFrame(exchangeinstance.fetchOHLCV(symbol,'1m',limit=limit,params=p))
        kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        kline.set_index('Time',inplace=True, drop=True)
        kline.index = pd.to_datetime(kline.index,unit='ms')
        kline = kline.resample(f'{multiplier}T').agg(ohlc_dict)
        return kline
    elif unit.lower() == 'h':
        kline = pd.DataFrame(exchangeinstance.fetchOHLCV(symbol,'1h',limit=limit,params=p))
        kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        kline.set_index('Time',inplace=True, drop=True)
        kline.index = pd.to_datetime(kline.index,unit='ms')
        kline = kline.resample(f'{multiplier}H').agg(ohlc_dict)
        return kline
    elif unit.lower() == 'd':
        kline = pd.DataFrame(exchangeinstance.fetchOHLCV(symbol,'1d',limit=limit,params=p))
        kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        kline.set_index('Time',inplace=True, drop=True)
        kline.index = pd.to_datetime(kline.index,unit='ms')
        kline = kline.resample(f'{multiplier}D').agg(ohlc_dict)
        return kline
    elif unit.lower() == 'w':
        kline = pd.DataFrame(exchangeinstance.fetchOHLCV(symbol,'1d',limit=limit,params=p))
        kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        kline.set_index('Time',inplace=True, drop=True)
        kline.index = pd.to_datetime(kline.index,unit='ms')
        kline = kline.resample(f'{multiplier}W').agg(ohlc_dict)
        return kline
####################klines####################
def klines(exchange, symbol, timeframe,limit=None):
    """Do not use limit for custom timeframes!!! """
    if exchange.lower() == 'binance':
        rates =['5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','w']
        exchangeinstance=ccxt.binance()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    if exchange.lower() == 'coinbase':
        rates=['5m','15m','1h','6h','1d']
        exchangeinstance=ccxt.coinbasepro()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF    
    if exchange.lower() == 'kraken':
        rates=['5m','15m','30m','1h','4h','1d','w']
        exchangeinstance=ccxt.kraken()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,None,rates)
        if limit != None:
            CMDF = CMDF.iloc[(-1*limit):]
        return CMDF
    if exchange.lower()== 'huobi':
        rates=['5m','15m','30m','1h','4h','1d','w']
        exchangeinstance=ccxt.huobipro()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    if exchange.lower() == 'kucoin':
        rates =['5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','w']
        exchangeinstance=ccxt.kucoin()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    if exchange.lower() == 'okex':
        rates =['5m','15m','30m','1h','2h','4h','6h','12h','1d','w']
        exchangeinstance=ccxt.okex()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    # if exchange.lower()=='bitfinex':
    #     rates=['5m','15m','30m','1h','3h','6h','12h','1d','w']
    #     exchangeinstance=ccxt.bitfinex()
    #     exchangeinstance.enableRateLimit = True
    #     CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates,p={'sort':-1})
    #     return CMDF
    if exchange.lower()== 'gemini':
        rates=['5m','15m','30m','1h','6h','1d']
        exchangeinstance=ccxt.gemini()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    if exchange.lower()== 'bitmax':
        rates =['5m','15m','30m','1h','2h','4h','6h','12h','1d','w']
        exchangeinstance=ccxt.bitmax()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    if exchange.lower()== 'bitstamp':
        rates =['5m','15m','30m','1h','2h','4h','6h', '12h','1d','w']
        exchangeinstance=ccxt.bitstamp()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates)
        return CMDF
    if exchange.lower() == 'forex':
        CMDF = forex(symbol,timeframe,limit)
        return CMDF
####################Date Converter####################
def parse_rfc3339(dt):
    import re
    broken = re.search(r'([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(\.([0-9]+))?(Z|([+-][0-9]{2}):([0-9]{2}))', dt)
    return datetime.datetime(
        year = int(broken.group(1)),
        month = int(broken.group(2)),
        day = int(broken.group(3)),
        hour = int(broken.group(4)),
        minute = int(broken.group(5)),
        second = int(broken.group(6)))

####################forex####################
def forex(symbol, timeframe, limit):
    rates =['5m','10m','15m','30m','1h','2h',
             '3h', '4h','6h','8h','12h','1d','w']
    import oandapyV20
    import oandapyV20.endpoints.instruments as instruments
    client = oandapyV20.API(access_token=oandatoken)
    symbol = symbol.replace('/','_')
    unit = timeframe[-1]
    multiplier = timeframe[:-1]
    ohlc_dict = {                                                                                                             
          'Open':'first',                                                                                                    
          'High':'max',                                                                                                       
          'Low':'min',                                                                                                        
          'Close': 'last'}
    if timeframe in rates:
        conversion = {'5m':'M5','10m': 'M10','15m':'M15','30m':'M30',
                  '1h':'H1','2h':'H2','3h':'H3','4h':'H4','6h':'H6',
                  '8h':'H8','12h':'H12','1d':'D','w':'W'}
        converted = conversion[timeframe]
        params = {"count": limit, "granularity": converted }
        r = instruments.InstrumentsCandles(instrument=symbol, params=params)
        a = client.request(r)
        a = a['candles']
        a = pd.DataFrame(a)
        a['time']=a['time'].apply(parse_rfc3339)
        b = a['mid'].apply(pd.Series)
        a = a.drop(['volume', 'complete', 'mid'], axis=1)
        a = a.join(b)
        a = a.rename({'time':'Time','o':'Open','h':'High','l':'Low','c':'Close'},axis=1)
        a.set_index('Time',inplace=True, drop=True)
        a["Close"] = pd.to_numeric(a["Close"])
        a["Open"] = pd.to_numeric(a["Open"])
        a["High"] = pd.to_numeric(a["High"])
        a["Low"] = pd.to_numeric(a["Low"])
        return a
    else:
        if unit.lower() == 'm':
            params = {"count": limit, "granularity": "M1"}
            r = instruments.InstrumentsCandles(instrument=symbol, params=params)
            a = client.request(r)
            a = a['candles']
            a = pd.DataFrame(a)
            a['time']=a['time'].apply(parse_rfc3339)
            b = a['mid'].apply(pd.Series)
            a = a.drop(['volume', 'complete', 'mid'], axis=1)
            a = a.join(b)
            a = a.rename({'time':'Time','o':'Open','h':'High','l':'Low','c':'Close'},axis=1)
            a.set_index('Time',inplace=True, drop=True)
            a = a.resample(f'{multiplier}T').agg(ohlc_dict)
            a["Close"] = pd.to_numeric(a["Close"])
            a["Open"] = pd.to_numeric(a["Open"])
            a["High"] = pd.to_numeric(a["High"])
            a["Low"] = pd.to_numeric(a["Low"])
            return a
        if unit.lower() == 'h':
            params = {"count": limit, "granularity": "H1"}
            r = instruments.InstrumentsCandles(instrument=symbol, params=params)
            a = client.request(r)
            a = a['candles']
            a = pd.DataFrame(a)
            a['time']=a['time'].apply(parse_rfc3339)
            b = a['mid'].apply(pd.Series)
            a = a.drop(['volume', 'complete', 'mid'], axis=1)
            a = a.join(b)
            a = a.rename({'time':'Time','o':'Open','h':'High','l':'Low','c':'Close'},axis=1)
            a.set_index('Time',inplace=True, drop=True)
            a = a.resample(f'{multiplier}H').agg(ohlc_dict)
            a["Close"] = pd.to_numeric(a["Close"])
            a["Open"] = pd.to_numeric(a["Open"])
            a["High"] = pd.to_numeric(a["High"])
            a["Low"] = pd.to_numeric(a["Low"])
            return a
        if unit.lower() == 'd':
            params = {"count": limit, "granularity": "D"}
            r = instruments.InstrumentsCandles(instrument=symbol, params=params)
            a = client.request(r)
            a = a['candles']
            a = pd.DataFrame(a)
            a['time']=a['time'].apply(parse_rfc3339)
            b = a['mid'].apply(pd.Series)
            a = a.drop(['volume', 'complete', 'mid'], axis=1)
            a = a.join(b)
            a = a.rename({'time':'Time','o':'Open','h':'High','l':'Low','c':'Close'},axis=1)
            a.set_index('Time',inplace=True, drop=True)
            a = a.resample(f'{multiplier}D').agg(ohlc_dict)
            a["Close"] = pd.to_numeric(a["Close"])
            a["Open"] = pd.to_numeric(a["Open"])
            a["High"] = pd.to_numeric(a["High"])
            a["Low"] = pd.to_numeric(a["Low"])
            return a
        if unit.lower() == 'w':
            params = {"count": limit, "granularity": "W"}
            r = instruments.InstrumentsCandles(instrument=symbol, params=params)
            a = client.request(r)
            a = a['candles']
            a = pd.DataFrame(a)
            a['time']=a['time'].apply(parse_rfc3339)
            b = a['mid'].apply(pd.Series)
            a = a.drop(['volume', 'complete', 'mid'], axis=1)
            a = a.join(b)
            a = a.rename({'time':'Time','o':'Open','h':'High','l':'Low','c':'Close'},axis=1)
            a.set_index('Time',inplace=True, drop=True)
            a = a.resample(f'{multiplier}W').agg(ohlc_dict)
            a["Close"] = pd.to_numeric(a["Close"])
            a["Open"] = pd.to_numeric(a["Open"])
            a["High"] = pd.to_numeric(a["High"])
            a["Low"] = pd.to_numeric(a["Low"])
            return a