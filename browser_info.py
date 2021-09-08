import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random

headers = {
    "user-agent": user,
}

link = 'https://browser-info.ru/'

# запрос к url
response = requests.get(link, headers=headers).text

# подключение библиотеки soup
soup = BeautifulSoup(response, "lxml")

# поиск корневого элемента блока по id
block = soup.find('div', id='tool_padding')

# parse on/off js in site
check_js = block.find('div', id='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

# parse flash in site
check_flash = block.find('div', id='flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

# parse user agent in site
check_user_agent = block.find('div', id='user_agent').text

print(result_js)
print(result_flash)
print(check_user_agent)
