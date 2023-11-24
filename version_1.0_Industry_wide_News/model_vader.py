import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from preprocessing_for_vader import preprocess_for_vader

# Download the VADER lexicon
nltk.download('vader_lexicon')


# Initialize VADER
sia = SentimentIntensityAnalyzer()

def get_summed_polarity_scores(titles):
    """
    Get the summed polarity scores for a list of texts.

    Args:
    titles (list of str): The list of texts to analyze.

    Returns:
    dict: A dictionary with summed 'neg', 'neu', 'pos', and 'compound' scores.
    """
    # Initialize total scores
    total_scores = {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}

    for title in titles:
        scores = sia.polarity_scores(title)
        for key in total_scores:
            total_scores[key] += scores[key]

    return total_scores
