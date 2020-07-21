import bs4

htm_str = "<html>hi<div>hello</div></html>"
result = bs4.BeautifulSoup(htm_str,'html.parser')

print(result.find('div').text)