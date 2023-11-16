'''
News Title Abstraction for The_defiant

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
    url = 'https://thedefiant.io/news'
    name = 'The_defiant'
    soup = connection(url, name)

    news_collector = []

    # News Explorer
    # Caption for Scrolling News
    scorlling_titles = soup.find_all('h3', class_='font-heading')
    scorlling_texts = soup.find_all('div', class_='font-body')

    # Extract the text or title from each span
    for title, text in zip(scorlling_titles, scorlling_texts):
        full_news = title.text + ': ' + text.text
        news_collector.append(full_news)


    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
