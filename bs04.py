import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = urllib.request.urlopen(url)

bs = BeautifulSoup(html,'html.parser')
#print(bs.find('div', {'class':'today'}))
#<div class="today">
today = bs.find_all('a', {'class' : 'nav'})
print(today)
#<a class="nav" href="https://section.cafe.naver.com/" data-clk="svc.cafe">카페</a>
for a in today:
    print(a.text)