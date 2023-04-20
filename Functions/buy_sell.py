def buysell(userobject,strategyclass):
    if userobject.DF['Strategy Name'] == strategyclass.strategyname:
        strategyname=strategyclass.strategyname
        telegramid = userobject.telegramid
        pairname = userobject.DF['Pair Name']
        exchange=userobject.DF['Exchange']
        longs=userobject.DF['Longs']
        shorts=userobject.DF['Shorts']
        buysellsignal={'Exchange':exchange,
                   'Buy':[],
                   'Sell':[],
                   'Strategy Name':strategyname,
                   'Pair Name':pairname,
                   'Telegram id':telegramid}
        for long in longs:
            if strategyclass.filtercriteria(exchange,long)==True:
                if strategyclass.longcriteria(exchange,long)==True:
                    buysellsignal['Buy'].append(long)
        for short in shorts:
            if strategyclass.filtercriteria(exchange,short)==True:
                if strategyclass.shortcriteria(exchange,short)==True:
                    buysellsignal['Sell'].append(short)


#Buy/Sell Function
def buysell(longs, shorts, strategy_class):
  buy = []
  sell = []
  for x in longs:
    if strategy_class.coinfilter(x) and strategy_class.longcriteria(x):
      buy.append(x)
  for y in shorts:
    if strategy_class.coinfilter(y) and strategy_class.shortcriteria(y):
       sell.append(y)
  dic = {'Buy' : buy, 'Sell' : sell, 'Strategy' : strategy_class.strategyname}
  return dic