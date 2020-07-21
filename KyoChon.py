from selenium import webdriver
from itertools import count
import time
from bs4 import BeautifulSoup

result = []
url = 'http://www.kyochon.com/shop/domestic.asp?sido1=0&sido2=0&txtsearch='
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
driver.execute_script('shop.getList(0)')
rcv_data = driver.page_source
soupData = BeautifulSoup(rcv_data, 'html.parser')
for span in soupData.findAll('span', {'class':"store_item"}):
    tr_tag = list(span.strings)
    store_name = tr_tag[1]
    store_address = tr_tag[3]
    store_sido_gu = store_address.split()[:2]
    store_phone = tr_tag[5]
    if store_phone != '':
        print(result.append([store_name]+store_sido_gu+[store_address]+[store_phone]))
import pandas as pd
KyoChon_table = pd.DataFrame(result, columns = ['store', 'sido', 'gungu','address', 'phone'])
KyoChon_table.to_csv("KyoChon.csv",encoding ='cp949', index=True)
print("교촌매장 주소 저장 완료")