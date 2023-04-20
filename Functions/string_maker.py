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