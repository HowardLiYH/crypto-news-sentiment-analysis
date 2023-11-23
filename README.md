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


## Version 1.0 Industry-wide News Sources  ✅
- The Scraping was conducted with Beautiful Soup from the stationary front page News Titles of 42 News Sites ✅
- News titles: Over 1400 Total New Titles will be obtained in each iteration ✅
- NLP Model of choice: VADER ✅


## Version 1.5 Token-specific News Sources 
- Given the input token name to search for Token-specific News from the 42 News Sites
- Gather ❓ amount of data for each search
- Calculate each token's weighted sentiment given the below formulas
<br />

**The $`ith`$  Industry-wide News Source Polarity Score:** $$S_i(Industry)$$
**The $`ith`$  Token-specific News Source Polarity Score:** $$S_i(Token)$$
**The $`Total`$  Industry-wide News Source Polarity Score:** $$S_{Total}(Industry) = \sum_{i=1}^m |S_i(Industry)|$$
**The $`Weighted`$ Token-specific News Source Polarity Score:** $$S_{weighted}(Token) = \sum_{i=1}^m [ \log \frac{S_i(Industry)}{S_{Total}(Industry)} + \log S_i(Token)]$$


## Version 2.0  Model Upgrade
- Considering fine-tuning an advanced word embedding method of choice (BERT): [CryptoBERT](https://huggingface.co/ElKulako/cryptobert)
- Conduct a Robustness Test (if possible)

  
## Version 2.5 More Sources
- Website Views: Use Selenium to go to Similarweb Website Analysis Dashboard (Google "Similar Web traffic checker" if need to ). Then scrape the recent month's views.
- YouTube Comments: Since Twitter and Reddit API are prohibited from free use, we can consider using YouTube API to search for "Today" News choose the top five results from the search, and scrape their comment sections to produce a general sentiment from the viewers. 

  
## Version 3.0 Deployment
- Streamlit for display



