import bs4
html_str = '''
<html>
    <body>
        <ul class = "great">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
'''
result = bs4.BeautifulSoup(html_str)
print(result.find_all('li'))
for li in result.find_all('li'):
        print(li.text)