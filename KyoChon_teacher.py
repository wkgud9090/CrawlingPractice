import urllib.request
from bs4 import BeautifulSoup
import pandas as pd 
from itertools import count 
from Get_URL import get_request_url

result = []
#for pageNum in count():
def getKyochonAddress(sido1, result):
    for sido2 in count():
        url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%s&sido2=%s&txtsearch=' %(str(sido1), str(sido2))
        print(url)
        try:
            rcv_data = get_request_url(url)
            soupData = BeautifulSoup(rcv_data, 'html.parser')
            spans = soupData.findAll('span', {'class':"store_item"})
            for span in spans:
                span = list(span.strings)
                store = span[1]
                address = span[3].strip()
                sido_gungu = address.split()[:2]
                phone = span[5].strip()
                #print([store] +sido_gungu+[address]+[phone])
                result.append([store] +sido_gungu+[address]+[phone])
        except Exception as e:
            print("행정구역 완료")
            break
    return    

if __name__ == "__main__":
    for sido1 in range(1, 18):
        getKyochonAddress(sido1, result)
    import pandas as pd 
    kyochon_table = pd.DataFrame(result, columns=['store','sido','gungu','address','phone'])
    kyochon_table.to_csv('kyochon.csv', encoding="cp949", index=True)
    print("교춘 매장 주소 저장 완료")