'''
News Title Abstraction for Cointelegraph

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
    url = 'https://cointelegraph.com/'
    name = 'Cointelegraph'
    soup = connection(url, name)

    news_collector = []

    # Titles on the top of the website (Total: 4)

    top_pos_titles = soup.find_all('span', class_='uni-block__name')
    # Extract the text or title from each span
    for title in top_pos_titles:
        news_collector.append(title.text)


    # Including Editor Choice and Hot Stories (Total: 10)
    main_pos_titles = soup.find_all('a', class_='main-news-controls__link')
    # Extract the text or title from each span
    for title in main_pos_titles:
        news_collector.append(title.text)

    # Press Release and Market Release (Total: 42)

    press_titles = soup.find_all('p', class_='ltr:ml-3 rtl:mr-3 text-sm flex-grow font-semibold text-zinc-800')
    # Extract the text or title from each span
    for title in press_titles:
        news_collector.append(title.text)

    # The Center News with Large Images (Total: 30)

    center_titles = soup.find_all('span', class_='post-card__title')
    center_texts = soup.find_all('p', class_='post-card__text')

    # Extract the text or title from each span
    for title, text in zip(center_titles, center_texts):
        full_news = title.text + ':' + text.text
        news_collector.append(full_news)




    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
