'''
News Title Abstraction for Theconversation

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
    url = 'https://theconversation.com/global/topics/blockchain-11427'
    name = 'Theconversation'
    soup = connection(url, name)

    news_collector = []

    # News Explorer
    explorer_titles = soup.find_all('h2')
    explorer_contexts = soup.find_all('div', class_='content')

    # Extract the text or title from each span
    for title, context in zip(explorer_titles, explorer_contexts):
        full_news = title.text.strip() + ': ' + context.text.strip()
        news_collector.append(full_news)


    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
