def signalmaker(raw_series,strategy_class):
    
    """
    Parameters
    ----------
    raw_series : Pandas Series
        Each row of the pair Dataframe from base user object:
        Indices: 'Exchange', 'Longs', 'Shorts', 'Pair Name', 'Strategy Name' 
    strategy_class : Class
        Strategy class with the matching name.
        
    Returns
    -------
    Signal Series.
    """
    
    buy=[]
    sell=[]
    logging.debug('buy and sell empty lists initiated')
    if raw_series['Longs']:
        for x in raw_series['Longs']:
            logging.debug('long pair detected')
            fcriteria= strategy_class.filtercriteria(raw_series['Exchange'],x)
            logging.debug('filter criteria applied')
            lcriteria= strategy_class.longcriteria(raw_series['Exchange'],x)
            logging.debug('long criteria applied')
            if fcriteria and lcriteria:
                buy.append(x)
                logging.debug('added to buy list')
        
    if raw_series['Shorts']:
        for y in raw_series['Shorts']:
            logging.debug('short pair detected')
            fcriteria= strategy_class.filtercriteria(raw_series['Exchange'],y)
            logging.debug('filter criteria applied')
            scriteria= strategy_class.shortcriteria(raw_series['Exchange'],y)
            logging.debug('short criteria applied')
            if fcriteria and scriteria:
                sell.append(y)
                logging.debug('added to sell list')
    
    signal_series= {'Exchange': raw_series['Exchange'],
                    'Longs': buy, 'Shorts': sell,
                    'Pair Name': raw_series['Pair Name'],
                    'Strategy': raw_series['Strategy']} 
    logging.debug('signal series created')
    return signal_series


###############alt###############
def signalmaker2(row):
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