from bs4 import BeautifulSoup
import requests

base = 'https://ru.stackoverflow.com'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id='question-mini-list')
a = div.find('a', class_='s-link')
parent = a.find_parent()
print(parent)
# for i in a:
#     print(i.getText(), base + i.get('href'))
