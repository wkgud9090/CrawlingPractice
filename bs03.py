import requests
import bs4

url = 'https://finance.naver.com/item/main.nhn?code=252670'

html = requests.get(url)
bs = bs4.BeautifulSoup(html.content,'html.parser')
#print(bs.find('div', {'class':'today'}))
#<div class="today">
today = bs.find('div', {'class' : 'today'})
print(today.find('span').text)