def threader(userobject):
    pairs=userobject.pairs
    userid=userobject.userid
    telegramid = userobject.telegramid
    s0 = datechecker(userobject)
    if s0:
        if type(pairs) == pd.DataFrame:
            for i in range(len(pairs.index)):
                t = threading.Thread(target=wrapper,args=(userid,pairs.iloc[i],telegramid))
                t.start()                    
        elif type(pairs) == pd.Series:
            wrapper(userid,pairs,telegramid)