'''
News Title Abstraction for Blockchainmagazine

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
    url = 'https://blockchainmagazine.net/'
    name = 'Blockchainmagazine'
    soup = connection(url, name)

    news_collector = []

    # News Explorer
    explorer_titles = soup.find_all('a', class_='mtc stc_h')

    titles = []
    # Extract the text or title from each span
    for title in explorer_titles:
        titles.append(title.text.strip())

    # Context Explorer
    explorer_context = soup.find_all('div', class_='stm_news_grid__excerpt')

    contexts = []
    # Extract the text or title from each span
    for title in explorer_context:
        contexts.append(title.text.strip())

    for i in range(len(titles) - len(contexts)):
        contexts.append(" ")

    for title, context in zip(titles, contexts):
        full_news = title + ": " + context
        news_collector.append(full_news)



    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
