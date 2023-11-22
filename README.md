# crypto-news-sentiment-analysis

![sentiment_pointer](https://camo.githubusercontent.com/fd0f81957c4db8f54e6b0069be9ce68ab497c795813e1c14bc2c62d79df6469e/68747470733a2f2f7777772e6d61726b65746d6f746976652e636f6d2f6d61726b65745f6d6f746976652f73656e74696d656e742d616e616c797369732e6a7067).

### Part I. News Source
- The Scraping was conducted with Beautiful Soup from the stationary front page News Titles of over 40 News Sites
- Over 1400 Total New Titles will be obtained in each iteration
- For JSON Page Scraping will be TBD in the future

### Part II. Model Selection
- NLP Model of choice: VADER (for now)
- Considering fine-tuning an advanced word embedding methods of choice (BERT or RoBERTa, GPT-2 or GPT-3)
- Robustness Test: TBD


### Part III. Deployment
- Setting Up a Web Framework
     - Framework: Django
     - Create a Web Application: defining routes, templates, and static files
- Streaming Data to the Website
     - API Endpoint: Create an API endpoint in your web application that returns the scraped data, usually in JSON format.
     - Updating Data: Decide on a method to update the data. It could be a scheduled task (using something like Celery) or triggered by user action.
     - Front-end Development: Use JavaScript (possibly with a library/framework like React or Vue.js) to fetch and display the streamed data on the client side.
- Deployment
     - Choose a Hosting Service: Options include Heroku, AWS, or Google Cloud.
     - Deploy Your Application: Follow the hosting service’s guidelines to deploy your web application.
