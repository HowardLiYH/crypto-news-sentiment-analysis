'''
Core Functions for News Aggregation

1. connection(url, name)

'''


import requests
from bs4 import BeautifulSoup



def connection(url, name):
    '''
    Inputs:
        url: the target url link of the news website
        name: the name of the news website
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
