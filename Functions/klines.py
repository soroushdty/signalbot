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