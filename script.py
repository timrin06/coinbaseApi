from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
ser = Service("G:\!Timur\Desktop\coinbaseApi\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=options)
driver.get('https://www.coinbase.com/ru/price/shiba-inu')
time.sleep(2)

main_page = driver.page_source
soup = BeautifulSoup(main_page, 'lxml')
quotes = soup.find_all('span', class_='AssetChartAmount__Number-sc-1b4douf-1 foyTCz')
quote = quotes[0].text
quote = quote.replace(',', '.')
quote = quote.replace('₽', '')
quote = quote.replace(' ', '')

print(quote)
driver.quit()
