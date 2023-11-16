'''
News Title Abstraction for Marketwatch

'''
import sys
import os

# Calculate the path to the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Initiate the news scraping
from connection_func import connection

def get_news_titles():
    '''
    Inputs:
        url: the target url link of the news website
        name: the name of the news website
    Output:
        news_collector: all the news titles obtainable from the site
    '''
    url = 'https://www.marketwatch.com/investing/cryptocurrency'
    name = 'Marketwatch'
    soup = connection(url, name)

    news_collector = []

    # News Explorer
    explorer_titles = soup.find_all('a')


    # Extract the text or title from each span
    for title in explorer_titles:
        if len(title.text.strip()) > 50:
            news_collector.append(title.text.strip())


    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
