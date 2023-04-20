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