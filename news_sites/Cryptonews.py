'''
News Title Abstraction for Cryptonews

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
    url = 'https://cryptonews.com/news/blockchain-news/'
    name = 'Cryptonews'
    soup = connection(url, name)

    news_collector = []

    # News Explorer
    explorer_titles = soup.find_all('a', class_='article__title article__title--lg article__title--featured mb-20')


    # Extract the text or title from each span
    for title in explorer_titles:
        news_collector.append(title.text.strip())

    # News Explorer
    recommended_titles = soup.find_all('a', class_='article__title article__title--recommended mb-0')


    # Extract the text or title from each span
    for title in recommended_titles:
        news_collector.append(title.text.strip())

    # News Explorer
    featured_titles = soup.find_all('a', class_='article__title article__title--md article__title--featured')


    # Extract the text or title from each span
    for title in featured_titles:
        news_collector.append(title.text.strip())



    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
