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
        pass