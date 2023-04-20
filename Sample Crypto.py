#Imports
import pandas as pd
import talib as ta
import ccxt
import datetime
import time
import pytz
import telegram

#Exchange
exchange = ccxt.binance()

#Timezone
tz=pytz.timezone('Asia/Tehran')

#Telegram properties
bottoken = '1319419042:AAEFxuRxXZBH6TkGCUlaY0WAHZ4R3lVanP8'
chatid = '@hdjebi24322'

#Pairs
long_list = ['ADA/USDT','AION/USDT','ALGO/USDT','ANKR/USDT','ARDR/USDT','ARPA/USDT',
             'ATOM/USDT','BAND/USDT','BAT/USDT','BCH/USDT','BEAM/USDT','BNB/USDT',
             'BNT/USDT','BTC/USDT','BTS/USDT','BTT/USDT','CELR/USDT', 'CHR/USDT','CHZ/USDT',
             'COCOS/USDT','COMP/USDT','COS/USDT','COTI/USDT','CTSI/USDT','CTXC/USDT',
             'CVC/USDT','DASH/USDT','DATA/USDT','DENT/USDT','DOCK/USDT','DOGE/USDT',
             'DREP/USDT','DUSK/USDT','ENJ/USDT','EOS/USDT','ERD/USDT','ETC/USDT',
             'ETH/USDT','FET/USDT','FTM/USDT','FTT/USDT','FUN/USDT','GTO/USDT','GXS/USDT',
             'HBAR/USDT','HC/USDT','HIVE/USDT','HOT/USDT','ICX/USDT','IOST/USDT',
             'IOTA/USDT','IOTX/USDT','KAVA/USDT','KEY/USDT','KNC/USDT','LEND/USDT',
             'LINK/USDT','LRC/USDT','LSK/USDT','LTC/USDT','LTO/USDT','MATIC/USDT',
             'MBL/USDT','MCO/USDT','MDT/USDT','MFT/USDT','MITH/USDT','MTL/USDT','NANO/USDT',
             'NEO/USDT','NKN/USDT','NPXS/USDT','NULS/USDT', 'OGN/USDT','OMG/USDT','ONE/USDT',
             'ONG/USDT','ONT/USDT','PERL/USDT','PNT/USDT','QTUM/USDT','REN/USDT','REP/USDT',
             'RLC/USDT','RVN/USDT','STMX/USDT', 'STPT/USDT','STRAT/USDT','STX/USDT',
             'TCT/USDT','TFUEL/USDT','THETA/USDT','TOMO/USDT','TROY/USDT','TRX/USDT',
             'VET/USDT','VITE/USDT','WAN/USDT','WAVES/USDT','WIN/USDT','WRX/USDT','WTC/USDT',
             'XLM/USDT','XMR/USDT','XRP/USDT','XTZ/USDT','XZC/USDT','ZEC/USDT','ZIL/USDT','ZRX/USDT']
short_list = ['ADA/USDT','ATOM/USDT','BAT/USDT','BCH/USDT','BNB/USDT','BTC/USDT',
              'DASH/USDT','EOS/USDT','ETC/USDT','ETH/USDT','IOST/USDT','IOTA/USDT',
              'LINK/USDT','LTC/USDT','MATIC/USDT','NEO/USDT','ONT/USDT','QTUM/USDT',
              'RVN/USDT','TRX/USDT','VET/USDT','XLM/USDT','XMR/USDT','XRP/USDT','XTZ/USDT','ZEC/USDT']

#Klinecleaner Function
def klinecleaner(coin,timeframe):
  kline = pd.DataFrame(exchange.fetchOHLCV(coin,timeframe,limit=50))
  kline.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
  kline.set_index('Time',inplace=True, drop=True)
  for column in kline:
    kline[column]=pd.to_numeric(kline[column])
  kline.index = pd.to_datetime(kline.index,unit='ms')
  return kline

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

#Duplichecker Function
def duplichecker(buyselldict):
  global fullfilledl
  global fullfilleds
  Long =[]
  Short = []
  for x in buyselldict['Buy']:
    if x not in fullfilledl:
      Long.append(x)
      fullfilledl.append(x)
  for x in buyselldict['Sell']:
    if x not in fullfilleds:
      Short.append(x)
      fullfilleds.append(x)
  for x in fullfilledl:
    if x not in buyselldict['Buy']:
      fullfilledl.remove(x)
  for x in fullfilleds:
    if x not in buyselldict['Sell']:
      fullfilleds.remove(x)  
  d = {'Long' : Long, 'Short' : Short, 'Strategy' : buyselldict['Strategy']}
  return d
 
 
 
#Stringmaker Function
def stringmaker(signaldict):
  longslist = []
  shortslist = []
  nl = "\n"
  if len(signaldict['Long']) != 0:
    for x in signaldict['Long']:
      longslist.append(x)
  if len(signaldict['Short']) != 0:
    for x in signaldict['Short']:
      shortslist.append(x)
  longstring = nl.join(longslist)
  shortstring = nl.join(shortslist)
  one = "***Strategy: "
  two = str(signaldict['Strategy'])
  star = "***"
  three = "\n***New Longs***\n"
  four = "\n***New Shorts***\n"
  signalstr = one + two + star + three + longstring + four + shortstring
  if longslist and shortslist:
    return signalstr
  else:
    return None
 
 
#Telegram Function
def telemessager(signalstring):
  if signalstring != None:
    bot = telegram.Bot(token=bottoken)
    bot.send_message(chat_id=chatid, text= signalstring, timeout=100000)
 
 
#Loop 'n' Log Function
def loopnlog(wrapper_function,sleep_time):
    global fullfilledl
    global fullfilleds
    while True:
        try:
            now = datetime.datetime.now(tz=tz)
            print(f'*Started at {now.strftime("%d %b %H:%M:%S")}*')
            wrapper_function()
        except Exception as exception:
            now = datetime.datetime.now(tz=tz)
            print(f'--Error: {type(exception).__name__} at {now.strftime("%d %b %H:%M:%S")}--')
            #fullfilled global variables reset
            fullfilledl = []
            fullfilleds = []
            time.sleep(sleep_time)
            pass
        else:
            now = datetime.datetime.now(tz=tz)
            print(f'*Completed at {now.strftime("%d %b %H:%M:%S")}*')
            time.sleep(sleep_time)
            pass

#fullfilled global variables reset
fullfilledl = []
fullfilleds = []

#EMACross Strategy Class
class EMACross:
  strategyname = "EMACross" 
  def coinfilter(coin):
    kline = klinecleaner(coin, '5m')
    vol = kline['Volume']
    if vol[-2]> 1000:
      return True
    else:
      return False
  def longcriteria(coin):
    #Define Hourly MACD histogram
    klineH = klinecleaner(coin, '1h')
    hcloh = (klineH['Close']+klineH['Open']+klineH['High']+klineH['Low'])/4
    MACD = ta.MACD(hcloh)
    MACDH = MACD[2]
    #Define 5m EMAs
    klineM = klinecleaner(coin, '5m')
    mix = (klineM['Close']+klineM['Open']+klineM['High']+klineM['Low'])/4
    ema10 = ta.EMA(mix,10)
    ema20 = ta.EMA(mix,20)
    if MACDH[-1]>=MACDH[-2] and ema10[-1]>ema20[-1]:
        return True
    else:
        return False
  def shortcriteria(coin):
    #Define Hourly MACD histogram
    klineH = klinecleaner(coin, '1h')
    hcloh = (klineH['Close']+klineH['Open']+klineH['High']+klineH['Low'])/4
    MACD = ta.MACD(hcloh)
    MACDH = MACD[2]
    #Define 5m EMAs
    klineM = klinecleaner(coin, '5m')
    mix = (klineM['Close']+klineM['Open']+klineM['High']+klineM['Low'])/4
    ema10 = ta.EMA(mix,10)
    ema20 = ta.EMA(mix,20)
    if MACDH[-1]<=MACDH[-2] and ema10[-1]<ema20[-1]:
        return True
    else:
        return False
    
#Wrapper Function
def wrapper():
  s1 = buysell(long_list,short_list,EMACross)
  s2 = duplichecker(s1)
  s3 = stringmaker(s2)
  telemessager(s3)
 
 
#Loop 'n' Log
loopnlog(wrapper, 300)