import requests
from bs4 import BeautifulSoup

image_number = 0
page_number = 0
url = f'https://zastavok.net/'

pagination_url = requests.get(url).text
pagination_soup = BeautifulSoup(pagination_url, 'lxml')
end_pagination = pagination_soup.find('div', id='clsLink3')

# last pagination number
link_pagination = int(end_pagination.find_all('a')[-2].text)

for storage in range(link_pagination):

    response = requests.get(f'{url}/{page_number}').text
    soup = BeautifulSoup(response, 'lxml')

    block = soup.find('div', class_='block-photo')
    all_img = block.find_all('div', class_='short_full')

    for image in all_img:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{url}{image_link}').text

        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = download_soup.find('div', class_='image_data').find('div', class_='block_down')
        result_link = download_block.find('a').get('href')

        # download image .content method
        image_byte = requests.get(f'{url}{result_link}').content

        with open(f'image/{image_number}.jpg', 'wb') as file:
            file.write(image_byte)

        image_number += 1

        print(f'Изображение №{image_number}.jpg скачано')

    page_number += 1
