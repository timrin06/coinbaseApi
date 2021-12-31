from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
#from user_agent import generate_user_agent
#from coinbase.wallet.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from datetime import datetime

#client = Client('Su2KNCgW9bZIw9Pp', 'XxTyWtwPou05c52MWc2L7sdu9GRoIlLG', api_version='YYYY-MM-DD')
#currency_code = 'USD'ydata = []

ydata = []
ydata_ma = []
ydata_ma1 = []
long_ydata_ma = []
long_ydata_ma1 = []

bank = {
    'cash' : 100000,
    'coin' : 0,
    'status' : False
}

i = int(input('i = '))
i1 = int(input('i1 = '))
long_i = int(input('long_i = '))
long_i1 = int(input('long_i1 = '))
file = input('file = ')

text = open('G:/!Timur/Desktop/coinbaseApi/' + file)
for line in text:
    price = line.split(',')
    price = price[len(price)-1]
    
    ydata.append(float(price))
    
    if long_i != 1:
         if len(ydata) > long_i:
            list_ma = ydata[len(ydata)-long_i:len(ydata)-1]
            long_ydata_ma.append(float(sum(list_ma)) / len(list_ma))
    else:
        long_ydata_ma.append(ydata[len(ydata)-1])
    if len(ydata) > long_i1:
        list_ma1 = ydata[len(ydata)-long_i1:len(ydata)-1]
        long_ydata_ma1.append(float(sum(list_ma1)) / len(list_ma1))
        
    if i > 1:        
        if len(ydata) > i:
            list_ma = ydata[len(ydata)-i:len(ydata)-1]
            ydata_ma.append(float(sum(list_ma)) / len(list_ma))
    else:
        ydata_ma.append(ydata[len(ydata)-1])
    if len(ydata) > i1:
        list_ma1 = ydata[len(ydata)-i1:len(ydata)-1]
        ydata_ma1.append(float(sum(list_ma1)) / len(list_ma1))
        
    if len(ydata) > long_i1:
        if long_ydata_ma[len(long_ydata_ma)-1] > long_ydata_ma1[len(long_ydata_ma1)-1]:            
            if ydata_ma[len(ydata_ma)-1] > ydata_ma1[len(ydata_ma1)-1] and bank['status'] == False:
                bank['status'] = True
                bank['coin'] = bank['cash'] / float(price)
                bank['cash'] = 0
                #print('buy' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
            if ydata_ma[len(ydata_ma)-1] < ydata_ma1[len(ydata_ma1)-1] and bank['status'] == True:
                bank['status'] = False
                bank['cash'] = bank['coin'] * float(price)
                bank['coin'] = 0
                #print('sell' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
        if long_ydata_ma[len(long_ydata_ma)-1] < long_ydata_ma1[len(long_ydata_ma1)-1] and bank['status'] == True:
            bank['status'] = False
            bank['cash'] = bank['coin'] * float(price)
            bank['coin'] = 0
            #print('sell' + '||' + str(bank['cash']) + '||' + str(bank['coin']))
             
    #print(bank)
if bank['coin'] != 0:
    bank['cash'] = bank['coin'] * ydata[len(ydata)-1]

print(bank)
