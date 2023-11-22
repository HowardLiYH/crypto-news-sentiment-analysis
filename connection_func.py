'''
Core Functions for News Aggregation

1. connection(url, name)

'''

import sys
import os
import glob
import requests
from bs4 import BeautifulSoup



def connection(url, name):
    '''
    Inputs:
        url: the target url link of the news website
        name: the name of the news website (Here included for Debug Purpouses)
    Ouputs:
        soup: the varibale from BeautifulSoup for parse content
        A message will be printed if the connection is established
    '''

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the website
    response = requests.get(str(url), headers=headers, timeout=30)

    # Check if the request was successful
    if response.status_code == 200:
        # print(f'Successful connected to {name}')
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

    else:
        print(f'Failed to retrieve the webpage with statsus code {response.status_code}')
    return soup



def news_collecting():
    # Add the module_directory to the sys.path
    MODULE_DIR = os.path.join(os.getcwd(), 'news_sites')
    sys.path.append(MODULE_DIR)

    news_titles_all = []
    news_titles_channel_specific = {}

    # Use glob to find all .py files in module_directory
    pattern = os.path.join(MODULE_DIR, "*.py")

    news_titles_all = []

    COUNT = 0
    for filepath in glob.glob(pattern):
        COUNT += 1
        # Extract the module name from the filepath
        module_name = os.path.basename(filepath)[:-3]  # Remove the '.py' from the end

        print('------------------------------------------------------------------')
        print(f'Connecting to Site No.{str(COUNT)}: {module_name.title()}')

        # Import the module using its name
        module = __import__(module_name)
        news_titles_channel_specific[f'{module_name.title()}'] = []

        try:
            # If the module has an attribute get_news_titles, call it and extend the list
            if hasattr(module, 'get_news_titles'):
                news_titles = module.get_news_titles()
                news_titles_channel_specific[f'{module_name.title()}'].append(news_titles)
                news_titles_all.extend(news_titles)
        except Exception as e:
            print(f"An error occurred {e} when obtaining News Data from {module_name}.")
            continue

    return news_titles_all, news_titles_channel_specific
