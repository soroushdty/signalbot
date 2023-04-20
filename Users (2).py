from my_cs import User, buysell
from kliner import klinecleaner
import talib as ta
import pandas as pd
        
user0=User('zero',0,'@dianaty_paydar',None,None,None,
           '2020/08/11')
user0.DF=pd.Series({'Exchange':'Binance',
'Longs': ['BTC/USDT','ETH/BTC','LINK/USDT', 'FET/USDT', 'ETH/USDT'],
'Shorts':['ETH/USDT', 'EOS/USDT','LTC/USDT','BCH/USDT','ADA/USDT'],
'Pair Name':None, 'Strategy Name':'EMA Cross'})
class EMACross:
    strategyname='EMA Cross'
    def __init__(self,exchange,symbol):
        self.exchange=exchange
        self.symbol=symbol
        self.timer=300
        self.kline=klinecleaner(exchange,symbol,timeframe='1h',limit=25)
        self.close = self.kline['Close']
        self.volume = self.kline['Volume']
        self.ema10 = ta.EMA(self.close,10)
        self.ema20=ta.EMA(self.close,20)
        def filtercriteria(self):
            if self.volume[-1]>1000: 
                return True
            else:
                return False
        def longcriteria(self):
            if self.ema10[-2]<self.ema20[-2] and self.ema10[-1]>self.ema20[-1]: 
                return True
            else:
                return False
        def shortcriteria(self):
            if self.ema10[-2]>self.ema20[-2] and self.ema10[-1]<self.ema20[-1]: 
                return True
            else:
                return False

    # super(EMACross,self).__init__(exchange,symbol)
    # self.kline=klinecleaner(self.exchange,self.symbol,timeframe='1h',limit=25)
    # self.close=kline['Close']
    # volume = kline['Volume']
    # ema10 = ta.EMA(close,10)
    # ema20 = ta.EMA(close,20)
    # def pairfilter(self):
    #     if volume>1000: 
    #         return True
    #     else:
    #         return False
    # def longfilter(self):
    #     if ema10[-2]<ema20[-2] and ema10[-1]>ema20[-1]: 
    #         return True
    #     else:
    #         return False
    # def shortfilter(self):
    #     if ema10[-2]>ema20[-2] and ema10[-1]<ema20[-1]: 
    #         return True
    #     else:
    #         return False
        
    






