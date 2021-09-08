import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
}

resp = requests.get(url, headers=headers).text

soup = BeautifulSoup(resp, 'lxml')

tbody = soup.find('tbody')
coins = tbody.findAll('tr')

for coin in coins:
    name = coin.find(class_='cmc-link').get('href').replace("/currencies/", "")[:-1]
    price = coin.find(class_='sc-131di3y-0 cLgOOr')

    if price:
        print(f'{name}: {price.text}\n')
    else:
        price = coin.find_all('td')[-2].find('span').text
        print(f'{name}: {price}\n')
