from bs4 import BeautifulSoup
import requests

url = 'https://ithelp.ithome.com.tw/articles/10202103'
request = requests.get(url)
contents = request.content
print(contents)
file = open('1.html', 'w')

file.write(contents.decode('utf-8'))
