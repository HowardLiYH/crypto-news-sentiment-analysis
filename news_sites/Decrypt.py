'''
News Title Abstraction for Decrypt

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
    news_collector = []
    total_url = ['https://decrypt.co/', 'https://decrypt.co/news']
    for i in range(len(total_url)):
        url = total_url[i]
        name = 'Decrypt'
        soup = connection(url, name)

        if i == 0:
            # News Explorer
            explorer_titles = soup.find_all('h4', class_='text-base')

            # Eliminte 'YOUR HUB ACHIEVEMENT'
            explorer_titles = explorer_titles[:-1]
            # Extract the text or title from each span
            for title in explorer_titles:
                # print(title.text)
                news_collector.append(title.text)

        if i == 1:
            # Sliding News
            sliding_titles = soup.find_all('div', class_='grow')

            # Extract the text or title from each span
            for title in sliding_titles:
                # Split the string at the "·" character and take the first part
                cleaned_text = title.text.split('·')[0]
                # print(cleaned_text)
                news_collector.append(cleaned_text)

            # Lower Titles
            lower_titles = soup.find_all('span', class_='font-medium')

            # Extract the text or title from each span
            for title in lower_titles:
                # Split the string at the "·" character and take the first part
                # print(title.text)
                news_collector.append(title.text)


    print(f'Total of {len(news_collector)} News Titles from {name} has been successfully collected!\n')
    return news_collector
