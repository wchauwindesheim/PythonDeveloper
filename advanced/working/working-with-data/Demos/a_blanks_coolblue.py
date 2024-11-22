import requests
from bs4 import BeautifulSoup


def get_content():
    # url = input('Enter a URL: ')
    # url = 'https://www.amazon.com/Sony-Playstation-PS4-Black-Console/dp/B012CZ41ZA?crid=23TUS61WOGJBT&dib=eyJ2IjoiMSJ9.TF2Oo0yRLavtdx9Kyw5VZMv989BQxrP20A3mFw_vMNMwI-szObZOMoloHmL7t44G2QvNpeazumCOyOcWaKQiWBWCzTKeZ3WFb1J6rYkwv8wINJO8q0TyS8OHWBSk8OtzDAqyft1ZEPHOZR-cpuWk0hO9rc_9UJQqxUNjh67dSFcB7_-MBYMIkevcA0M-dgN0tI1jv7fXD6ACS9vMwS6Edm2POFTdFrQkr7x7gkFfDz0.3RPUYKdkZyCagHXJs_HaOTNcQ0JjKp7-ipBi-h7p_ik&dib_tag=se&keywords=playstation&qid=1732281759&sprefix=playstation%2Caps%2C211&sr=8-3'
    url = 'https://www.coolblue.nl/product/956915/apple-macbook-pro-14-inch-m4-10-core-cpu-10-core-gpu-16gb-512gb-spacezwart-qwerty.html'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}
    r = requests.get(url, headers=headers)
    return r.text

def main():
    content = get_content()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')

    external_links = soup.find_all('strong', {'class':['sales-price__current', 'js-sales-price-current']})
    # external_links = soup.find_all('strong'', {'class':['sales-price__current', 'js-sales-price-current']})

    found = False
    for i, link in enumerate(external_links, 1):
        found = True
        print(f'{i}. {link}')

    if not found:
        print('None found.')

main()