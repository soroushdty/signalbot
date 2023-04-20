####################prerequisites####################
from Classes import User, Strategy
from klines import klines
import talib as ta
####################user0####################
class User0(User):
    class EMACross(Strategy):
        def fitercriteria(exchange,symbol):
            k1h=klines(exchange,symbol,'1h',50)
            volume = k1h['Volume']
            if volume[-1]>10000:
                return True
            else:
                return False
        def longcriteria(exchange,symbol):
            k1h=klines(exchange,symbol,'1h',50)
            close1h=k1h['Close']
            ema10=ta.EMA(close1h,10)
            ema20=ta.EMA(close1h,20)
            if ema10[-1]>ema20[-1]:
                return True
            else:
                return False
        def shortcriteria(exchange,symbol):
            k1h=klines(exchange,symbol,'1h',50)
            close1h=k1h['Close']
            ema10=ta.EMA(close1h,10)
            ema20=ta.EMA(close1h,20)
            if ema10[-1]<ema20[-1]:
                return True
            else:
                return False
    

u0=User0('userzero',0,'@dianaty_paydar',None,None,None,'2020/08/15',
          [{'Exchange':'Binance',
    'Longs': ['BTC/USDT','ETC/USDT','LINK/USDT','LTC/USDT','NEO/USDT'],
    'Shorts': ['ETH/USDT','BCH/USDT','ADA/USDT','EOS/USDT','BTC/USDT'],
    'Pair Name': None,
    "Strategy Name": 'EMA Cross'},
    {'Exchange':'Binance',
    'Longs': ['BTC/USDT','ETC/USDT','LINK/USDT','LTC/USDT','NEO/USDT'],
    'Shorts': ['ETH/USDT','BCH/USDT','ADA/USDT','EOS/USDT','BTC/USDT'],
    'Pair Name': None,
    "Strategy Name": 'Elder'}])








from Functions import userlooper
userlooper([user0])