def duplichecker(signal_series):
    if fulfilled not in locals():
        logging.debug('First iteration')
        fulfilled = copy.deepcopy(signal_series)
        logging.debug('fulfilled created')
        
    else:
        for x in signal_series['Longs']:
            if x in fulfilled['Longs']:
                signal_series['Longs'].remove(x)
                logging.debug(f'{x} removed from final series')
            else:
                fulfilled['Longs'].append(x)
                logging.debug(f'{x} added to fulfilled')
            
        for i in fulfilled['Longs']:
            if i in signal_series['Longs']:
                fulfilled['Longs'].remove(i)
                logging.debug(f'{i} removed from fulfilled')
                
                
        for y in signal_series['Shorts']:
            if y in fulfilled['Shorts']:
                signal_series['Shorts'].remove(y)
                logging.debug(f'{y} removed from final series')
        else:
            fulfilled['Shorts'].append(y)
            logging.debug(f'{y} added to fulfilled')
        
        for j in fulfilled['Shorts']:
            if j in signal_series['Shorts']:
                fulfilled['Shorts'].remove(j)
                logging.debug(f'{j} removed from fulfilled')
    final_series= signal_series
    logging.debug('Output renamed')
    return final_series


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