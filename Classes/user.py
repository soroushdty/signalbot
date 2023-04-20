class User:
    """
        Parameters
        ----------
        username : string : Arbitrary username.
        
        userid : int : Unique user id.
        
        telegramid : string : User telegram id including @.
        
        email : string
        
        subscription : string : User subscription type.
        
        expire : string : Expiration date in form of 2020/06/15.
        
        pairs : dict or list of dicts:
            {'Exchange': string,
            'List Name': None or string
            'Longs': list of strings,
            'Shorts': list of strings,
            'Strategy': object of the strategy class}

        Returns
        -------
        User Object
        """
          
    def __init__(self, username, userid, telegramid, email,
                 subscription, expiration,pairs):

        self.username = username
        self.userid = userid
        self.telegramid = telegramid
        self.email = email
        self.subscription = subscription
        self.expiration = expiration
        #Convert dict into pandas Series and list of dicts into pandas DataFrame
        if type(pairs)==dict:
            self.pairs=pd.Series(pairs)
        elif type(pairs)==list:
            self.pairs=pd.DataFrame(pairs)