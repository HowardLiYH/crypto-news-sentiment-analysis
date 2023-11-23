# 🐂 crypto-news-sentiment-analysis 🧸

![sentiment_pointer](https://camo.githubusercontent.com/fd0f81957c4db8f54e6b0069be9ce68ab497c795813e1c14bc2c62d79df6469e/68747470733a2f2f7777772e6d61726b65746d6f746976652e636f6d2f6d61726b65745f6d6f746976652f73656e74696d656e742d616e616c797369732e6a7067)

## Setup Instructions

To set up the environment for this project, please follow these steps:

- Clone the repository
```
git clone https://github.com/HowardLiYH/crypto-news-sentiment-analysis.git
```
- Navigate to the project directory:
```
cd crypto-news-sentiment-analysis
```
- Install the required dependencies:
```
pip install -r requirements.txt
```
After completing these steps, your environment will be set up with all the necessary dependencies! 🙆

<br />
<br />

## Version 1.0 Industry-wide News Sources  ✅
**Target Platform:** 42 News Sites 
- Cointelegraph, The Block, Decrypt, The Defiant, CoinDesk, Blockworks, Blockchain News, BeInCrypto, CNBC Blockchain News, Blockchain.com, Yahoo News Crypto Section, Techcrunch Blockchain Section, Economic Times, Forbes
- Financial Times, Independent, The blockchain.com, The Conversation, Cryptonews, Wired, Fox Business, Crypto News Net, AP News, The Indian Express, The Time of India, BBC News, News Now, Blockchain Magazine
- CCN, Washington Post, New York Times, Bezinga, Google News, New York Post, People.com, NBC News, Daily Mail, The Guardian, Wall Street Journal, Buzzfeed, MarketWatch, Fortune 

<br />

**Methodology:** 

Scraping over 42 News Sites with Beautiful Soup and collecting Crypto-related News Titles from the selected pages. Each iteration can obtain over 1400 the most recent New Titles.

<br />

**Model:** 

[NLTK.sentiment.vader](https://www.nltk.org/_modules/nltk/sentiment/vader.html)

<br />

**Result:** 

Output Top Five Most Bullish Websites and Top Five Most Bearish Websites computed by [VADER's compound polarity score](https://github.com/cjhutto/vaderSentiment) 
```
The compound score is computed by summing the valence scores of each word in the lexicon, adjusted according to the
rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive).

This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence.
Calling it a 'normalized, weighted composite score' is accurate.

It is also useful for researchers who would like to set standardized thresholds for classifying sentences as either
positive, neutral, or negative. Typical threshold values (used in the literature cited on this page) are:

positive sentiment: compound score >= 0.05
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
negative sentiment: compound score <= -0.05
NOTE: The compound score is the one most commonly used for sentiment analysis by most researchers,
including the authors.
```


<br />
<br />

## Version 2.0 Token-specific News Sources & Industry-wide News Aggregation
- Given the input token name to search for Token-specific News from the 42 News Sites
- Gather ❓ amount of data for each search
- Calculate each token's weighted sentiment given the below formulas
<br />

**The $`ith`$  Industry-wide News Source Polarity Score:** $$S_i(Industry)$$
**The $`ith`$  Token-specific News Source Polarity Score:** $$S_i(Token)$$
**The $`Total`$  Industry-wide News Source Polarity Score:** $$S_{Total}(Industry) = \sum_{i=1}^m |S_i(Industry)|$$
**The $`Weighted`$ Token-specific News Source Polarity Score:** $$S_{weighted}(Token) = \sum_{i=1}^m [ \log \frac{S_i(Industry)}{S_{Total}(Industry)} + \log S_i(Token)]$$

<br />
<br />

## Version 2.2  Model Upgrade
- Considering fine-tuning an advanced word embedding method of choice (BERT): [CryptoBERT](https://huggingface.co/ElKulako/cryptobert)
- Conduct a Robustness Test (if possible)

<br />
<br />
  
## Version 2.5 More Sources
- Website Views: Use Selenium to go to Similarweb Website Analysis Dashboard (Google "Similar Web traffic checker" if need to ). Then scrape the recent month's views.
- YouTube Comments: Since Twitter and Reddit API are prohibited from free use, we can consider using YouTube API to search for "Today" News choose the top five results from the search, and scrape their comment sections to produce a general sentiment from the viewers. 


<br />
<br />

## Version 3.0 Deployment
- Streamlit for display



