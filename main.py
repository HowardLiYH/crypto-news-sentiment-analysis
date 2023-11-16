'''
This is the main file for performing News Aggregation
'''

import sys
import os
import glob

# Add the module_directory to the sys.path
MODULE_DIR = os.path.join(os.getcwd(), 'news_sites')
sys.path.append(MODULE_DIR)


news_titles_all = []

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

    try:
        # If the module has an attribute get_news_titles, call it and extend the list
        if hasattr(module, 'get_news_titles'):
            news_titles = module.get_news_titles()
            news_titles_all.extend(news_titles)
    except Exception as e:
        print(f"An error occurred {e} when obtaining News Data from {module_name}.")
        continue

print('------------------------------------------------------------------')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(f'Total Number Websites Scraped: {str(COUNT)}')
print(f'Total Number News Titles Obtained: {len(news_titles_all)}')

# news_titles_all now contains all the titles from all the Python files


# # Now news_titles_all has all the news titles.

# # Perform sentiment analysis
# sentiments = analyze_sentiment(news_titles_all)

# # Process the sentiment results as needed
# ...
