import urllib.request
from bs4 import BeautifulSoup
import pandas as pd 
from itertools import count 


result = []
for pageNum in count():

    url = 'https://pelicana.co.kr/store/stroe_search.html?page=%s' % str(pageNum+1)
    response = urllib.request.urlopen(url)
    soupData = BeautifulSoup(response, 'html.parser')
    table = soupData.find('table', {'class':"table mt20"})
    tbody = table.find('tbody')
    #print(tbody)
    #print(list(tbody.find_all('tr')[0].strings))
    #store  = list(tbody.find_all('tr')[0].strings)
    beEnd = True 
    for store in tbody.find_all('tr'):
        beEnd = False
        tr_tag = list(store.strings)
        store_name = tr_tag[1]
        store_addr = tr_tag[3]
        store_phone = tr_tag[5].strip()
        store_sido_gu = tr_tag[3].split()[:2]
        result.append([store_name]+[store_sido_gu]+[store_addr]+[store_phone])
    if beEnd : 
        break
    print("페리카나 [%s] 페이지 크롤링중" % (str(pageNum+1)))

#print(result)



pelicana_table = pd.DataFrame(result, columns=['store', 'sido','gungu','address', 'phone'])
pelicana_table.to_csv('pelicana.csv', encoding='cp949', index=True)
