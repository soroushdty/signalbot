####################prerequisites####################
import ccxt
import pandas as pd
import datetime
oandatoken = 'cb95230707ff3a32e562677cf56929d8-256d5fb01977813c733077b1188f896b'
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
            return a
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
    if exchange.lower() == 'forex':
        CMDF = forex(symbol,timeframe,limit)
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
    if exchange.lower()=='bitfinex':
        rates=['5m','15m','30m','1h','3h','6h','12h','1d','w']
        exchangeinstance=ccxt.bitfinex()
        CMDF = ohlcgrabber(exchangeinstance,symbol,timeframe,limit,rates,p={'sort':-1})
        return CMDF
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