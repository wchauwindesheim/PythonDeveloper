from urllib.request import Request, urlopen

req = Request(
    url='https://www.coolblue.nl/product/956915/apple-macbook-pro-14-inch-m4-10-core-cpu-10-core-gpu-16gb-512gb-spacezwart-qwerty.html', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
print(webpage)