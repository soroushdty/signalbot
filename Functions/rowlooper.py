def rowlooper(userobject): 
    strategy_list = [a for a in userobject.__dict__.values() if type(a)==type]
    logging.debug('Strategy list created')
    if type(userobject.pairs)==pd.Dataframe:
        logging.debug('Type DataFrame')
        for x in range(len(userobject.pairs.index)):
            for y in strategy_list:
                if userobject.pairs.iloc[x].Strategy==y.strategyname:
                    logging.info('')
                    threading.Thread(target=inner_wrapper, args=(userobject.pairs.iloc[x],y,userobject.pairs.iloc[x].telegramid))
    elif type(userobject.pairs)==pd.Series:
        for y in strategy_list:
                if userobject.pairs.Strategy==y.strategyname:
                    logging.debug('Type Series')
                    threading.Thread(target=inner_wrapper, args=(userobject.pairs,y,userobject.pairs.telegramid))
                    logging.info(f'Inner thread started for user{userobject.userid}')