import requests

url = 'https://static.webucator.com/media/public/documents/hrleaders.html'
r = requests.get(url)
content = r.text
print(content[:125]) # print first 125 characters