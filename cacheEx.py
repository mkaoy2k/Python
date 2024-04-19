import requests
import random
from cacheLib import *

# User provides how to populate the cache


def get_url(url):
    """Check cache prior to visiting HTTP server"""
    print("===>Getting URL...")

    # Check cache if it is already in
    if my_cache.has(url):
        # Page hit
        my_cache.inc(url)
        val_obj = my_cache.get(url)
    else:
        # Page fault: insert a new item to cache
        val_obj = get_url_from_server(url)
        my_cache.add(url, val_obj)

    # Return the 'val' object from the value
    return val_obj


def get_url_from_server(url):
    """Return text content of a given URL from a HTTP server"""
    print("===>Fetching URL from server...")
    try:
        response = requests.get(url, timeout=2.50)
        if response.status_code == requests.codes.ok:
            return response.text
    except:
        return None


# Main
if __name__ == '__main__':

    urls = ("https://invalid_url",
            "https://invalid_url2",
            "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/toolbox.py",
            "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/greetings.py",
            "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/README.md",
            "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/f845d66ac49fb2e17296da9078abdc3ace7a1632/1.0%20%E5%B0%8F%E6%9C%8B%E5%8F%8B%E7%8E%A9%E5%A4%A7%E8%9F%92%E8%9B%87%20-%20100%20pages.pdf",
            "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/1.0%20小朋友玩大蟒蛇.ipynb",
            "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/2.0%20小朋友玩大蟒蛇.ipynb"
            )

    # Instantiate a cache
    my_cache = Cache()

    # Test cache functions
    max_read = 100
    for count in range(max_read):
        url = random.choice(urls)
        print(f'{count}: Get {url}')
        val_str = str(get_url(url))
        print(f'===>URL: ...{val_str[5:50]}...\n')

    # Test cache Management functions
    print(f'Test cache Management functions...')
    print(f'{my_cache}\n')

    # Keep half of the cache in size with mostly-used items
    print(f'Keeping half of the cache in size with mostly-used items with no ref reset')
    my_cache.shrink(percent=50)
    print(f'{my_cache}\n')

    # Keep top 3  mostly-used items in the cache
    nbr = 3
    print(f'Keeping and resetting top {nbr} mostly-used items in the cache')
    my_cache.purge(size=nbr)
    print(f'{my_cache}\n')
