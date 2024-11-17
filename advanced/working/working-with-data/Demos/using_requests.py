import requests

url = 'https://oraculo.nl/itmg/python/hrleaders.html'
r = requests.get(url)
content = r.text
print(content[:125]) # print first 125 characters