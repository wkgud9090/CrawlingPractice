
import urllib.request
import datetime

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