import requests

data="https://oraculo.nl/itmg/python/hrleaders.json" 

r = requests.get(data)
records = r.json()

for i, record in enumerate(records, 1):
    player = record['Player']
    hrs = record['HR']
    year = record['Year']
    print(f'{i}. {player} hit {hrs} home runs in {year}.')