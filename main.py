## imports
import copy
import telegram
import threading
import time
import datetime
import logging
import pandas as pd
import ccxt
import pytz
import sys

# initiate variables
tz=pytz.timezone('Asia/Tehran')
bottoken= ''
logging.basicConfig(filename= 'log.log', level=logging.DEBUG, format='%(asctime)s:%(levelname):%messages')

#fullfilled global variables reset
fullfilledl = []
fullfilleds = []

#Loop 'n' Log
loopnlog(wrapper, 300)