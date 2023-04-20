class Strategy:
    """        
        This is the base class for user-defined strategies.
        All Strategy classes are inherited from this class
        and named in format of: 'User0_strategyname'.
        
        Parameters
        -------
        strategyname: string
        loop: int: looping interval in seconds

        Methods
        -------
        Override these methods at the level of inheritation:
        
        (1) def filtercriteria(self,exchange,symbol): #optional
        (2) def longcriteria(self,exchange,symbol):
        (3) def shortcriteria(self,exchange,symbol):
            
        Use the following convetion for writing strategies:
        (Candles) k5m = klines(exchange,symbol,'5m',limit=limit) #5m is the timeframe
        (Price) close5m = k5m['Close']
        (Indicator) ta.INDICATOR(close5m,*args)
        (Condition) if criteria:
                        return True
                    else:
                        return False
        """
    def __init__(self,strategyname,loop):
        self.strategyname=strategyname
        self.loop=loop
    def filtercriteria(self,exchange,symbol):
        return True
    def longcriteria(self,exchange,symbol):
        pass
    def shortcriteria(self,exchange,symbol):
        
        

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