import websockets
import json
import datetime
import time
import numpy as np
from coinbase.wallet.client import Client

client = Client('Su2KNCgW9bZIw9Pp', 'XxTyWtwPou05c52MWc2L7sdu9GRoIlLG', api_version='YYYY-MM-DD')
currency_code = 'USD'

bank = {
    'cash' : 100000,
    'coin' : 0,
    'status' : False
}

i = int(input('i = '))

while True:
    with open('db.json', 'r+') as f:
        db = json.load(f)
    ydata = db['ydata']
    ydata_ma = db['ydata_ma']
        
    priceSell = client.get_sell_price(currency=currency_code)
    priceSpot = client.get_sell_price(currency=currency_code)
    print(float(priceSpot.amount))

    ydata.append(float(priceSell.amount))
            
    if len(ydata) > i:
        list_ma = ydata[len(ydata)-i1:len(ydata)-1]
        ydata_ma.append(float(sum(list_ma)) / max(len(list_ma), 1))
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
    with open('db.json', 'w') as f:
            f.write(json.dumps(db))
            
    time.sleep(60)
