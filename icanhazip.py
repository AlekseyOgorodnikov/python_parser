import requests
import multiprocessing


def handler(proxy):
    link = 'http://icanhazip.com/'

    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {response.strip()}')
    except:
        print('Прокси не валидный')


with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, proxy_base)
