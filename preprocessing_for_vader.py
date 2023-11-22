'''
This is the preprocessing file for VADER sentiment analysis
'''


def preprocess_for_vader(titles):
    """
    Preprocess a list of news titles for VADER sentiment analysis:
    - Lowercasing (optional, depending on the case significance)
    - Removing excessive whitespace and line breaks
    - Removing empty titles

    Args:
    titles (list of str): The list of news titles to preprocess.

    Returns:
    list of str: A list of preprocessed news titles.
    """

    preprocessed_titles = []

    for title in titles:
        # Trim leading and trailing whitespace
        title = title.strip()
        # Skip empty titles
        if not title:
            continue
        # Convert to lowercase (optional for VADER)
        # title = title.lower()  # Uncomment if case normalization is needed
        # Remove excessive whitespace
        title = " ".join(title.split())

        preprocessed_titles.append(title)

    return preprocessed_titles
