import requests
from bs4 import BeautifulSoup


def get_content():
    # url = input('Enter a URL: ')
    url = 'https://www.amazon.com/Sony-Playstation-PS4-Black-Console/dp/B012CZ41ZA?crid=23TUS61WOGJBT&dib=eyJ2IjoiMSJ9.TF2Oo0yRLavtdx9Kyw5VZMv989BQxrP20A3mFw_vMNMwI-szObZOMoloHmL7t44G2QvNpeazumCOyOcWaKQiWBWCzTKeZ3WFb1J6rYkwv8wINJO8q0TyS8OHWBSk8OtzDAqyft1ZEPHOZR-cpuWk0hO9rc_9UJQqxUNjh67dSFcB7_-MBYMIkevcA0M-dgN0tI1jv7fXD6ACS9vMwS6Edm2POFTdFrQkr7x7gkFfDz0.3RPUYKdkZyCagHXJs_HaOTNcQ0JjKp7-ipBi-h7p_ik&dib_tag=se&keywords=playstation&qid=1732281759&sprefix=playstation%2Caps%2C211&sr=8-3'
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.amazon.com",
}    
    r = requests.get(url, headers=headers)
    return r.text

def main():
    content = get_content()
    with open('amazon.html', 'w', encoding="utf-8") as f:
        f.write(content)
    soup = BeautifulSoup(content, 'lxml')

    # external_links = soup.find_all('span', class_='a-offscreen')
    # external_links = soup.find_all('span', class_='a-price-whole')
    external_links = []
    div = soup.find('div', id='corePriceDisplay_desktop_feature_div')
    # print(div)

    soup = BeautifulSoup(str(div), 'lxml')
    price = soup.find('span', class_='a-price-whole')
    print(price.text)

    tags = soup.select(".a-price-whole, .a-price-fraction")
    
    print(tags[0].text, tags[1].text, sep='')
    # found = False
    # for i, link in enumerate(external_links, 1):
    #     found = True
    #     print(f'{i}. {link}')

    # if not found:
    #     print('None found.')

main()