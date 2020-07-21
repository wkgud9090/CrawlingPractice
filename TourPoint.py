import urllib.request
import datetime
import time
import math
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
def getTourPointVisitor(yyymm, sido, gungu, nPagenum, nItems):
    serviceKey = "400iA9ln1XUUO3jxGMYEKx0ce9vcpw23Ag5htvt0M1Kjiefy%2F1sRLNBogr0aDAjMT9zZ1B9FEsmSbTv19x4r1w%3D%3D"
    url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    parameter = '?_type=json&serviceKey=' + serviceKey
    parameter += '&YM=' + yyymm
    parameter += '&SIDO='+ urllib.parse.quote(sido)
    parameter += '&GUNGU=' + urllib.parse.quote('')
    parameter += '&RES_NM=&pageNo='+ str(nPagenum)
    parameter += '&numOfRows=' + str(nItems)

    url = url + parameter
    #print(url)
    retData = get_request_url (url)
    if retData == None:
        return None
    return json.loads(retData)


result = []

for year in range(2012, 2013):
    for month in range(1,13):
        yyyymm = "{0}{1:0>2}".format(str(year), str(month))
        nPagenum = 1
        while True:
            jsonData = getTourPointVisitor(yyyymm, '서울특별시','',nPagenum,100)
            print("%s 서울특별시 관광지 크롤링"% yyyymm)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                nTotal = jsonData['response']['body']['totalCount']
                if nTotal == 0 : break

                for item in jsonData['response']['body']['items']['item']:
                    sido ='' if 'sido' not in item.keys() else item['sido']
                    gungu = '' if 'gungu' not in item.keys() else item['gungu']
                    resNm = '' if 'resNum' not in item.keys() else item['resNum']
                    rnum =0 if 'rnum' not in item.keys() else item['rnum']
                    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
                    csForCnt = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
                    csNatCnt = 0  if 'csNatCnt' not in item.keys() else item['csNatCnt']
                    if 'csForCnt' in item.keys() :
                        result.append([yyyymm] + [sido] +[gungu]+[resNm] + [addrCd] + [csForCnt] + [csNatCnt])

                nPage = math.ceil(nTotal/100)
                if(nPagenum == nPage):
                    break
                nPagenum = nPagenum+1

            else:
                break


import pandas as pd 

pd.DataFrame(result, columns = ['year', 'sido', 'gungu','No', 'phone'])
pd.DataFrame(result).to_csv('tourpoint.csv', encoding='cp949', index=False)
