class User:           
    def __init__(self, username, userid, telegramid,
                 instagramid, email, subscription, expire):
        self.username = username
        self.userid = userid
        self.telegramid = telegramid
        self.instagramid = instagramid
        self.email = email
        self.subscription = subscription
        self.expire = expire
        #DF: A list of dictionaries with keys:
        #Exchange,Longs,Shorts,PairName, strategyname converted to pandas DataFrame
        
            

    """How to create a strategy object:
       (a) init
       (b) Override pairfilter method
       (c) Override longfilter method
       (d) Override shortfilter method
       Notice: This is where klinecleaner and ta-lib are used"""
# class Strategy:
#     """Set self.timer, set OHLCV and indicators, override criteria(exchange,symbol)"""
#     def __init__(self,exchange,symbol):
#         self.exchange = exchange
#         self.symbol = symbol
#         self.stategyname=''
#         self.timer = 0
#         #Initiate all
#     def filtercriteria(self):
#         if True: #filtercriteria
#             return True
#         else:
#             return False
#     def longcriteria(self):
#         if True: #longcriteria
#             return True
#         else:
#             return False
#     def shortcriteria(self):
#         if True: #shortcriteria
#             return True
#         else:
#             return False

        
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
        
        
    


