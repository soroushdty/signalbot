from Bcls import User,Strategy
from Bfuncs import threader,klines
import talib as ta

#First define an inheritance of Strategy class   class Userx_strategy
#Then instantiate the drived class   userx_strategy=Userx_strategy(name,loop)
#Then instantiate User class   userx=User(***)
#Start a threader terminal   threader(userx)

        
class EMACross(Strategy):
    def longcriteria(self,exchange,symbol):
        k1h=klines(exchange,symbol,'1h',50)
        hloc=(k1h['Close']+k1h['Open']+k1h['High']+k1h['Low'])/4
        EMA10=ta.EMA(hloc,10)
        EMA20=ta.EMA(hloc,20)
        if EMA20[-2]>=EMA10[-2] and EMA20[-1]<=EMA10[-1]:
            return True
        else:
            return False
    def shortcriteria(self,exchange,symbol):
        k1h=klines(exchange,symbol,'1h',50)
        hloc=(k1h['Close']+k1h['Open']+k1h['High']+k1h['Low'])/4
        EMA10=ta.EMA(hloc,10)
        EMA20=ta.EMA(hloc,20)
        if EMA20[-2]<=EMA10[-2] and EMA20[-1]>=EMA10[-1]:
            return True
        else:
            return False

long_list=['BTC/USDT',
 'ETH/USDT',
 'BNB/USDT',
 'BCC/USDT',
 'NEO/USDT',
 'LTC/USDT',
 'QTUM/USDT',
 'ADA/USDT',
 'XRP/USDT',
 'EOS/USDT',
 'IOTA/USDT',
 'XLM/USDT',
 'ONT/USDT',
 'TRX/USDT',
 'ETC/USDT',
 'ICX/USDT',
 'VEN/USDT',
 'NULS/USDT',
 'VET/USDT',
 'BCH/USDT',
 'BSV/USDT',
 'LINK/USDT',
 'WAVES/USDT',
 'BTT/USDT',
 'ONG/USDT',
 'HOT/USDT',
 'ZIL/USDT',
 'ZRX/USDT',
 'FET/USDT',
 'BAT/USDT',
 'XMR/USDT',
 'ZEC/USDT',
 'IOST/USDT',
 'CELR/USDT',
 'DASH/USDT',
 'NANO/USDT',
 'OMG/USDT',
 'THETA/USDT',
 'ENJ/USDT',
 'MITH/USDT',
 'MATIC/USDT',
 'ATOM/USDT',
 'TFUEL/USDT',
 'ONE/USDT',
 'FTM/USDT',
 'ALGO/USDT',
 'USDSB/USDT',
 'GTO/USDT',
 'ERD/USDT',
 'DOGE/USDT',
 'DUSK/USDT',
 'ANKR/USDT',
 'WIN/USDT',
 'COS/USDT',
 'NPXS/USDT',
 'COCOS/USDT',
 'MTL/USDT',
 'TOMO/USDT',
 'PERL/USDT',
 'DENT/USDT',
 'MFT/USDT',
 'KEY/USDT',
 'STORM/USDT',
 'DOCK/USDT',
 'WAN/USDT',
 'FUN/USDT',
 'CVC/USDT',
 'CHZ/USDT',
 'BAND/USDT',
 'BEAM/USDT',
 'XTZ/USDT',
 'REN/USDT',
 'RVN/USDT',
 'HC/USDT',
 'HBAR/USDT',
 'NKN/USDT',
 'STX/USDT',
 'KAVA/USDT',
 'ARPA/USDT',
 'IOTX/USDT',
 'RLC/USDT',
 'MCO/USDT',
 'CTXC/USDT',
 'BCH/USDT',
 'TROY/USDT',
 'VITE/USDT',
 'FTT/USDT',
 'OGN/USDT',
 'DREP/USDT',
 'TCT/USDT',
 'WRX/USDT',
 'BTS/USDT',
 'LSK/USDT',
 'BNT/USDT',
 'LTO/USDT',
 'STRAT/USDT',
 'AION/USDT',
 'MBL/USDT',
 'COTI/USDT',
 'STPT/USDT',
 'WTC/USDT',
 'DATA/USDT',
 'XZC/USDT',
 'SOL/USDT',
 'CTSI/USDT',
 'HIVE/USDT',
 'CHR/USDT',
 'GXS/USDT',
 'ARDR/USDT',
 'LEND/USDT',
 'MDT/USDT',
 'STMX/USDT',
 'KNC/USDT',
 'REP/USDT',
 'LRC/USDT',
 'PNT/USDT',
 'COMP/USDT',
 'BKRW/USDT',
 'SC/USDT',
 'ZEN/USDT',
 'SNX/USDT',
 'VTHO/USDT',
 'DGB/USDT',
 'SXP/USDT',
 'MKR/USDT',
 'DAI/USDT',
 'DCR/USDT',
 'STORJ/USDT',
 'MANA/USDT',
 'YFI/USDT',
 'BAL/USDT',
 'BLZ/USDT',
 'IRIS/USDT',
 'KMD/USDT',
 'JST/USDT',
 'SRM/USDT',
 'ANT/USDT',
 'CRV/USDT',
 'SAND/USDT',
 'OCEAN/USDT',
 'NMR/USDT',
 'DOT/USDT',
 'LUNA/USDT',
 'RSR/USDT',
 'WNXM/USDT',
 'TRB/USDT',
 'BZRX/USDT',
 'SUSHI/USDT',
 'YFII/USDT',
 'KSM/USDT',
 'EGLD/USDT',
 'DIA/USDT',
 'RUNE/USDT',
 'FIO/USDT',
 'UMA/USDT']
short_list=['BTC/USDT',
 'ETH/USDT',
 'BNB/USDT',
 'NEO/USDT',
 'LTC/USDT',
 'QTUM/USDT',
 'ADA/USDT',
 'XRP/USDT',
 'EOS/USDT',
 'IOTA/USDT',
 'XLM/USDT',
 'ONT/USDT',
 'TRX/USDT',
 'ETC/USDT',
 'ICX/USDT',
 'NULS/USDT',
 'VET/USDT',
 'BCH/USDT',
 'LINK/USDT',
 'WAVES/USDT',
 'BTT/USDT',
 'ONG/USDT',
 'ZIL/USDT',
 'ZRX/USDT',
 'FET/USDT',
 'BAT/USDT',
 'XMR/USDT',
 'ZEC/USDT',
 'IOST/USDT',
 'CELR/USDT',
 'DASH/USDT',
 'NANO/USDT',
 'OMG/USDT',
 'THETA/USDT',
 'ENJ/USDT',
 'MATIC/USDT',
 'ATOM/USDT',
 'TFUEL/USDT',
 'ONE/USDT',
 'FTM/USDT',
 'ALGO/USDT',
 'DOGE/USDT',
 'ANKR/USDT',
 'TOMO/USDT',
 'DOCK/USDT',
 'WAN/USDT',
 'CHZ/USDT',
 'BAND/USDT',
 'XTZ/USDT',
 'REN/USDT',
 'RVN/USDT',
 'HBAR/USDT',
 'KAVA/USDT',
 'ARPA/USDT',
 'IOTX/USDT',
 'RLC/USDT',
 'BCH/USDT',
 'TROY/USDT',
 'FTT/USDT',
 'OGN/USDT',
 'TCT/USDT',
 'WRX/USDT',
 'LSK/USDT',
 'BNT/USDT',
 'COTI/USDT',
 'WTC/USDT',
 'SOL/USDT',
 'CTSI/USDT',
 'HIVE/USDT',
 'CHR/USDT',
 'GXS/USDT',
 'LEND/USDT',
 'KNC/USDT',
 'REP/USDT',
 'LRC/USDT',
 'PNT/USDT',
 'COMP/USDT',
 'SC/USDT',
 'SNX/USDT',
 'VTHO/USDT',
 'DGB/USDT',
 'MKR/USDT',
 'STORJ/USDT',
 'MANA/USDT',
 'YFI/USDT',
 'BAL/USDT',
 'BLZ/USDT',
 'IRIS/USDT',
 'KMD/USDT',
 'JST/USDT',
 'SRM/USDT',
 'ANT/USDT',
 'CRV/USDT',
 'SAND/USDT',
 'DOT/USDT',
 'WNXM/USDT',
 'TRB/USDT',
 'BZRX/USDT',
 'SUSHI/USDT',
 'YFII/USDT',
 'KSM/USDT',
 'RUNE/USDT']
strategy1=EMACross('EMA Cross',0)

class BB(Strategy):
    def longcriteria(self,exchange,symbol):
        k=klines(exchange,symbol,'1h',50)
        hloc=(k['Open']+k['High']+k['Low']+k['Close'])/4
        bb=ta.BBANDS(hloc,timeperiod=20,matype=1)
        down=bb[2]
        if (k['Close'])[-2]<=down[-2] and (k['Close'])[-1]>=down[-1]:
            return True
        else:
            return False

    def shortcriteria(self,exchange,symbol):
        k=klines(exchange,symbol,'1h',50)
        hloc=(k['Open']+k['High']+k['Low']+k['Close'])/4
        bb=ta.BBANDS(hloc,timeperiod=20,matype=1)
        up=bb[0]
        if (k['Close'])[-2]>=up[-2] and (k['Close'])[-1]<=up[-1]:
            return True
        else:
            return False
        
class Stoch(Strategy):
    def longcriteria(self,exchange,symbol):
        k=klines(exchange,symbol,'1h',50)
        stoch=ta.STOCH(k['High'],k['Low'],k['Close'],fastk_period=14,slowk_matype=1,slowd_matype=1)
        slowk=stoch[0]
        if slowk[-2]<=20 and slowk[-1]>=20:
            return True
        else:
            return False
    def shortcriteria(self,exchange,symbol):
        k=klines(exchange,symbol,'1h',50)
        stoch=ta.STOCH(k['High'],k['Low'],k['Close'],fastk_period=14,slowk_matype=1,slowd_matype=1)
        slowk=stoch[0]
        if slowk[-2]>=80 and slowk[-1]<=80:
            return True
        else:
            return False
    
strategy2=BB('Bollinger Bands',0)
strategy3=Stoch('Stochastic',0)
soroush=User('Soroush',0,'@soroushdia', None,'trial','2021/09/08',
           [{'Exchange':'Binance',
             'List Name':None,
            'Longs':long_list ,
            'Shorts':short_list,
            'Strategy': strategy1},
            {'Exchange':'Binance',
             'List Name':None,
            'Longs':long_list ,
            'Shorts':short_list,
            'Strategy': strategy2},
            {'Exchange':'Binance',
             'List Name':None,
            'Longs':long_list ,
            'Shorts':short_list,
            'Strategy': strategy3}])