
import timeit
from timeit import repeat
import requests

FEED = 'https://data.buienradar.nl/2.0/feed/json'

params = {
}

def main():



    # r = requests.get(FEED, params)

    td1 = timeit.repeat("requests.get(FEED, params)", number=1, globals=globals())


    print("Results from using timeit()")
    print(td1)


main()