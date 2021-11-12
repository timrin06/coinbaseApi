from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.coinbase.com/ru/price/livepeer")
time.sleep(4)

main_page = driver.page_source
soup = BeautifulSoup(main_page, 'lxml')
quotes = soup.find_all('span', class_='AssetChartAmount__Number-sc-1b4douf-1 foyTCz')

print(quotes)
driver.quit()
