def stringmaker(final_series):
    final_string=''
    buys=''
    sells=''
    if final_series['Longs']==False and final_series['Shorts']==False:
        return None
    else:
        for x in final_series['Longs']:
            buys += x + '\n'
        for y in final_series['Shorts']:
            sells += y + '\n'
    
    if final_series['Longs'] and final_series['Shorts']:
        if final_series['Pair Name']:
            final_string ="""
***
Exchange: {}
Pair Selection: {}
Strategy: {}
Longs:
{}
Shorts:
{}
***""".format(final_series['Exchange'],final_series['Pairs'],final_series['Strategy'], buys, sells)
        else:
            final_string ="""
***
Exchange: {}
Strategy: {}
Longs:
{}
Shorts:
{}
***""".format(final_series['Exchange'],final_series['Strategy'], buys, sells)
    elif final_series['Longs'] and not final_series['Shorts']:
        if final_series['Pair Name']:
            final_string ="""
***
Exchange: {}
Pair Selection: {}
Strategy: {}
Longs:
{}
***""".format(final_series['Exchange'],final_series['Pairs'],final_series['Strategy'], buys)
        else:
            final_string ="""
***
Exchange: {}
Strategy: {}
Longs: 
{}
***""".format(final_series['Exchange'],final_series['Strategy'], buys)
    elif final_series['Shorts'] and not final_series['Longs']:
        if final_series['Pair Name']:
            final_string ="""
***
Exchange: {}
Pair Selection: {}
Strategy: {}
Shorts:
{}
***""".format(final_series['Exchange'],final_series['Pairs'],final_series['Strategy'], sells)
        else:
            final_string ="""
***
Exchange: {}
Strategy: {}
Shorts:
{}
***""".format(final_series['Exchange'],final_series['Strategy'], sells)
            
    return final_string




#alt
def stringmaker(signaldict):
    finalstring=''
    exchange=signaldict['Exchange']
    listname=signaldict['List Name']
    strategyname=signaldict['Strategy']
    
    buy =''
    if signaldict['Buy']:
        for x in signaldict['Buy']:
            buy='\n'+x+buy
    
    sell=''
    if signaldict['Sell']:
        for x in signaldict['Sell']:
            sell='\n'+x+sell
    
    if listname:
        if buy and sell:
            finalstring ="""
    ***
    Exchange: {}
    List Name: {}
    Strategy: {}
    Buys:{}
    Sells:{}
    ***
    """.format(exchange, listname, strategyname,buy,sell)
        elif buy and not sell:
            finalstring ="""
    ***
    Exchange: {}
    List Name: {}
    Strategy: {}
    Buys:{}
    ***
    """.format(exchange, listname, strategyname,buy)
        elif sell and not buy:
            finalstring ="""
    ***
    Exchange: {}
    List Name: {}
    Strategy: {}
    Sells:{}
    ***
    """.format(exchange,listname, strategyname,sell)
    else:
        if buy and sell:
            finalstring ="""
    ***
    Exchange: {}
    Strategy: {}
    Buys:{}
    Sells:{}
    ***
    """.format(exchange,strategyname,buy,sell)
        elif buy and not sell:
            finalstring ="""
    ***
    Exchange: {}
    Strategy: {}
    Buys:{}
    ***
    """.format(exchange,strategyname,buy)
        elif sell and not buy:
            finalstring ="""
    ***
    Exchange: {}
    Strategy: {}
    Sells:{}
    ***
    """.format(exchange,strategyname,sell)
    
    if finalstring:
        return finalstring
    else:
        return None






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