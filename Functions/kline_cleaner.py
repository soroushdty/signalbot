def klinecleaner(coin,timeframe):
  kline = pd.DataFrame(exchange.fetchOHLCV(coin,timeframe,limit=50))
  kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
  kline.set_index('Time',inplace=True, drop=True)
  for column in kline:
    kline[column]=pd.to_numeric(kline[column])
  kline.index = pd.to_datetime(kline.index,unit='ms')
  return kline