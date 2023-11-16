'''
News Title Abstraction for The_block

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
    url = 'https://www.theblock.co/'
    name = 'The_block'
    soup = connection(url, name)

    news_collector = []

    # News Explorer
    main_titles = soup.find_all('a', class_='appLink')

    for title in main_titles:
        if len(title.text) > 40:
            news_collector.append(title.text)

    # Top Right Access News Section

    top_right_titles = soup.find_all('a', class_='recArticle__titleWrapper')

    # Extract the text or title from each span
    for title in top_right_titles:
        news_collector.append(title.text)

    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
