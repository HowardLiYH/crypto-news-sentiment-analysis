# 🐂 crypto-news-sentiment-analysis 🧸

![sentiment_pointer](https://camo.githubusercontent.com/fd0f81957c4db8f54e6b0069be9ce68ab497c795813e1c14bc2c62d79df6469e/68747470733a2f2f7777772e6d61726b65746d6f746976652e636f6d2f6d61726b65745f6d6f746976652f73656e74696d656e742d616e616c797369732e6a7067)

## Version 1.0 Industry-wide News Sources  ✅
- **Target Platform:** 42 News Sites 
  - Cointelegraph, The Block, Decrypt, The Defiant, CoinDesk, Blockworks, Blockchain News, BeInCrypto, CNBC Blockchain News, Blockchain.com, Yahoo News Crypto Section, Techcrunch Blockchain Section, Economic Times, Forbes
  - Financial Times, Independent, The blockchain.com, The Conversation, Cryptonews, Wired, Fox Business, Crypto News Net, AP News, The Indian Express, The Time of India, BBC News, News Now, Blockchain Magazine
  - CCN, Washington Post, New York Times, Bezinga, Google News, New York Post, People.com, NBC News, Daily Mail, The Guardian, Wall Street Journal, Buzzfeed, MarketWatch, Fortune 

<br />

- **Methodology and Ouput:**
    - Scraping over 42 News Sites with Beautiful Soup and collecting Crypto-related News Titles from the selected pages. Each iteration can obtain over 1400 of the most recent New Titles. We attempted two NLP Models, [NLTK.sentiment.vader](https://www.nltk.org/_modules/nltk/sentiment/vader.html) and a Pre-trained Transformer Model [CryptoBERT](https://huggingface.co/ElKulako/cryptobert). We decided to proceed with the Transformer Model as it's trained on a wide range of crypto-related datasets and is fine-tuned specifically for crypto sentiment analysis. Our output will determine the sentiment bias of the 42 websites of our choice and rank the Top 5 Sites with Bullish sentiment and the Top 5 with Bearish sentiment.
    - Check out sample result in ouput_vader.ipynb and ouput_cryptobert.ipynb inside [Version 1.0 folder](https://github.com/HowardLiYH/crypto-news-sentiment-analysis/tree/main/version_1.0_Industry_wide_News)


<br />
<br />

## Version 2.0 Token News and Industry News Aggregation 🔜

**Target Platform:** 5 cryptocurrency market tracking websites
- CoinMarketCap, CoinGecko, Livecoinwatch.com, Coincodex, CryptoCompare

<br />

**Methodology:** 
- Obtain Coin-specific News from the above 5 platforms through APIs (if not attempt Selenium)
- Obtain Coin-specific Media Post (Twitter or Reddit) from the above 5 platforms through APIs (if not attempt Selenium)
- Obtain Industry News from the [Coincodex News Aggregation Site](https://coincodex.com/news/)
- Place Weights to the Polarity Score referenced from [Semrush](https://www.semrush.com/website/coinmarketcap.com/competitors/)

<br />

**Model:** 

- [CryptoBERT](https://huggingface.co/ElKulako/cryptobert) ✅


<br />

**Result:** TBA

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

## Version 3.0 GUI
- Streamlit for display



