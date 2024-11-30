import requests
from bs4 import BeautifulSoup


def get_content():
    # url = input('Enter a URL: ')
    url = 'https://www.coolblue.nl/product/956915/apple-macbook-pro-14-inch-m4-10-core-cpu-10-core-gpu-16gb-512gb-spacezwart-qwerty.html'
    # url = 'https://oraculo.nl/itmg/python/hrleaders.html'
    r = requests.get(url)
    return r.text

def main():
    content = get_content()
    soup = BeautifulSoup(content, 'lxml')

    # external_links = soup.find_all('a', target='_blank')
    external_links = soup.find_all('tr','steroids-era')

    found = False
    for i, link in enumerate(external_links, 1):
        found = True
        print(f'{i}. {link}')

    if not found:
        print('None found.')

main()