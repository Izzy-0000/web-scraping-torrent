from bs4 import BeautifulSoup as BS
import requests

url = 'https://ondebaixa.com/lost-download-via-torrent/'

response = requests.get(url)
soup = BS(response.text,'html.parser')

file = open('links.html', 'w')

for x in soup.find_all('a'):       
    if "magnet" in x.get('href'):
        print('======> {}\n'.format(x.get("href")))
        file.write("<a href='{}'> {} </a><hr>".format(x.get("href"), x.get("href")))

file.close()

