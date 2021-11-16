import json
import datetime
import time
import numpy as np
from coinbase.wallet.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

client = Client('Su2KNCgW9bZIw9Pp', 'XxTyWtwPou05c52MWc2L7sdu9GRoIlLG', api_version='YYYY-MM-DD')
currency_code = 'USD'

xdata = []
ydata = []

xdata_ma = []
ydata_ma = []

bank = {
    'cash' : 100000,
    'coin' : 0,
    'status' : False
}

i = int(input('i = '))

while True:
    #with open('db.json', 'r+') as f:
        #db = json.load(f)
    #ydata = db['ydata']
    #ydata_ma = db['ydata_ma']
        
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.coinbase.com/price/litecoin')
    time.sleep(3)

    main_page = driver.page_source
    soup = BeautifulSoup(main_page, 'lxml')
    quotes = soup.find_all('span', class_='AssetChartAmount__Number-sc-1b4douf-1 foyTCz')
    quote = quotes[0].text
    quote = quote.replace(',', '.')
    quote = quote.replace('₽', '')
    quote = quote.replace('\xa0', '')
    quote = quote.replace(' ', '')
    driver.quit()
    #priceSell = client.get_sell_price(currency=currency_code)
    priceSpot = quote
    print(float(quote))

    ydata.append(float(quote))
            
    if len(ydata) > i:
        list_ma = ydata[len(ydata)-i:len(ydata)-1]
        ydata_ma.append(float(sum(list_ma)) / max(len(list_ma), 1))
        if ydata[len(ydata)-1] > ydata_ma[len(ydata_ma)-1] and bank['status'] == False:    
            bank['status'] = True
            bank['coin'] = bank['cash'] / float(priceSpot)
            bank['cash'] = 0
            print('buy' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
        if ydata[len(ydata)-1] < ydata_ma[len(ydata_ma)-1] and bank['status'] == True:    
            bank['status'] = False
            bank['cash'] = bank['coin'] * float(priceSpot)
            bank['coin'] = 0
            print('sell' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
    print(bank)
    #with open('db.json', 'w') as f:
            #f.write(json.dumps(db))
            
    time.sleep(57)
