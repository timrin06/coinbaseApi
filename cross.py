from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from coinbase.wallet.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import datetime

client = Client('Su2KNCgW9bZIw9Pp', 'XxTyWtwPou05c52MWc2L7sdu9GRoIlLG', api_version='YYYY-MM-DD')
currency_code = 'USD'

ydata = []

ydata_ma = []

ydata_ma1 = []

bank = {
    'cash' : 100000,
    'coin' : 0,
    'status' : False
}

i = int(input('i = '))
i1 = int(input('i1 = '))
coin = input('coin = ')

t = datetime.now().minute

while True:
    if datetime.now().minute != t:
        #with open('db.json', 'r+') as f:
            #db = json.load(f)
        #ydata = db['ydata']
        #ydata_ma = db['ydata_ma']

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        ser = Service("G:\!Timur\Desktop\coinbaseApi\chromedriver.exe")
        driver = webdriver.Chrome(service=ser, options=options)
        driver.get('https://www.coinbase.com/price/'+coin)
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

        if i > 1:        
            if len(ydata) > i:
                list_ma = ydata[len(ydata)-i:len(ydata)-1]
                ydata_ma.append(float(sum(list_ma)) / len(list_ma))
        else:
            ydata_ma.append(ydata[len(ydata)-1])
        if len(ydata) > i1:
            list_ma1 = ydata[len(ydata)-i1:len(ydata)-1]
            ydata_ma1.append(float(sum(list_ma1)) / len(list_ma1))
            if ydata_ma[len(ydata_ma)-1] > ydata_ma1[len(ydata_ma1)-1] and bank['status'] == False:
                bank['status'] = True
                bank['coin'] = bank['cash'] / float(priceSpot)
                bank['cash'] = 0
                print('buy' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
            if ydata_ma[len(ydata_ma)-1] < ydata_ma1[len(ydata_ma1)-1] and bank['status'] == True:
                bank['status'] = False
                bank['cash'] = bank['coin'] * float(priceSpot)
                bank['coin'] = 0
                print('sell' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
        print(bank)
        #with open('db.json', 'w') as f:
                #f.write(json.dumps(db))
        
        t = datetime.now().minute

