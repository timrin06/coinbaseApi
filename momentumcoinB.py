import websockets
import asyncio
import json
import time
import datetime
#import matplotlib.pyplot as plt
import numpy as np
from coinbase.wallet.client import Client

client = Client('Su2KNCgW9bZIw9Pp', 'XxTyWtwPou05c52MWc2L7sdu9GRoIlLG', api_version='YYYY-MM-DD')
currency_code = 'USD'

xdata = []
ydata = []

xdata_ma = []
ydata_ma = []

xdata_ma1 = []
ydata_ma1 = []

xdata_ma2 = []
ydata_ma2 = []

bank = {
    'cash' : 100000,
    'coin' : 0,
    'status' : False
}

i1 = int(input('i1 = '))

while True:    
    priceSell = client.get_sell_price(currency=currency_code)
    priceSpot = client.get_sell_price(currency=currency_code)
    print(float(priceSpot.amount))

    xdata.append(datetime.datetime.now())
    ydata.append(float(priceSell.amount))
            
    if len(xdata) > i1:
        list_ma = ydata[len(ydata)-i1:len(ydata)-1]
        ydata_ma.append(float(sum(list_ma)) / max(len(list_ma), 1))
        xdata_ma.append(xdata[len(xdata)-1])                
        if ydata[len(ydata)-1] > ydata_ma[len(ydata_ma)-1] and bank['status'] == False:    
            bank['status'] = True
            bank['coin'] = bank['cash'] / float(priceSpot.amount)
            bank['cash'] = 0
            print('buy' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
        if ydata[len(ydata)-1] < ydata_ma[len(ydata_ma)-1] and bank['status'] == True:    
            bank['status'] = False
            bank['cash'] = bank['coin'] * float(priceSpot.amount)
            bank['coin'] = 0
            print('sell' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
    print(bank)
    time.sleep(60)
