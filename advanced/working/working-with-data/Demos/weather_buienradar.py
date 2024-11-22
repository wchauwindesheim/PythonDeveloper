import requests
from datetime import datetime

FEED = 'https://data.buienradar.nl/2.0/feed/json'


def main():


    params = {
    }

    r = requests.get(FEED, params)
    print(r.url) # prints the URL created using the params

    weather = r.json()

    lijst = weather['actual']['stationmeasurements']

    for item in lijst:
        print(item['stationname'])
        print(item['temperature'])

    # fmt_in = '%Y-%m-%d %H:%M:%S'
    # fmt_out = '%A, %B %d, %Y at %I %p'
    # for item in weather['list']:
    #     max_temp = item['main']['temp_max']
    #     dt = item['dt_txt']
    #     day_time = datetime.strptime(dt, fmt_in).strftime(fmt_out)
    #     print(f'High on {day_time} in {city}: {max_temp} fahrenheit.')

main()