import urllib.request
import datetime
import time
import json

def get_request_url(url, enc='utf-8'):        
    req = urllib.request.Request(url)
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc,'replace')
            return ret
    except Exception as e:
        print(e) 
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


def getNatVisitor(yyyymm, nat_cd, ed_cd):
    serviceKey="8Uhyf4%2BYK9gKfK3XNj2lX3M9IuRAzUZfJC8IJo45p5fNCtDUiRDYfVbuNXccsn%2FdAzhAxFnCUmjgeHP3lQsZLw%3D%3D"

    endpoint ='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameters = '?_type=json&serviceKey='+ serviceKey
    parameters += '&YM=' + yyyymm
    parameters += '&NAT_CD='+ nat_cd
    parameters += '&ED_CD=' + ed_cd
    url = endpoint + parameters
    #print(url)
    retData = get_request_url(url)
    if retData == None : 
        return None
    else:
        return json.loads(retData) 
    
    
result = []
for year in range(2015, 2016):
    for month in range(1,13):
        yyyymm = '{0}{1:0>2}'.format(str(year),str(month) )
        jsonData = getNatVisitor(yyyymm, "275", "E")
        #print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False)) 

        if(jsonData['response']['header']['resultMsg'] == 'OK'):
            krName = jsonData['response']['body']['items']['item']['natKorNm']
            krName = krName.replace(' ','')
            iTotalVisit = jsonData['response']['body']['items']['item']['num']
            print("%s_%s : %s" %(krName,yyyymm, iTotalVisit))
            result.append([yyyymm]+[krName]+['275']+[iTotalVisit])

import pandas as pd 
pd.DataFrame(result).to_csv('%s_해외방문자_%s'%('275','2015')+'.csv',
        encoding='cp949',header=None, index =False)

cnVistit = []
visitYM = []
index = []
i = 0
for item in result:
    index.append(i)
    cnVistit.append(item[3])
    visitYM.append(item[0])
    i=i+1

import matplotlib.pyplot as plt
import matplotlib

plt.xticks(index, visitYM)
plt.plot(index, cnVistit)
plt.grid(True)
plt.show()

