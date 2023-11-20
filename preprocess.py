'''
Source: Natural Language Processing with Probabilistic Models, Week 1, Coursera Assignment

Description:

1) process_data: read the file, convert all letters to lower case, and return a list of words.

2) get_count: return a dictionary where the keys are words, and the values are the number of times each word appears in the file.

3) get_probs: return a dictionary where the keys are words, and the values are the probability that a word will occur. To calculate the values divide the frequency of each word by the sum of the frequencies of all words.
'''


import re

def process_data(file_name):
    """
    Input:
        A file_name which is found in your current directory. You just have to read it in.
    Output:
        words: a list containing all the words in the corpus (text file you read) in lower case.
    """
    words = [] # return this variable correctly


    #Open the file, read its contents into a string variable
    with open(file_name) as f:
        file_name_data = f.read()
    # convert all letters to lower case
    file_name_data = file_name_data.lower()
    #Convert every word to lower case and return them in a list.
    words = re.findall('\w+',file_name_data)

    return words

def get_count(word_l):
    '''
    Input:
        word_l: a set of words representing the corpus.
    Output:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    '''

    word_count_dict = {}  # fill this with word counts
    for i in word_l:
        word_count_dict[i] = word_count_dict.get(i, 0) + 1
    return word_count_dict

def get_probs(word_count_dict):
    '''
    Input:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    Output:
        probs: A dictionary where keys are the words and the values are the probability that a word will occur.
    '''
    probs = {}  # return this variable correctly


    # get the total count of words for all words in the dictionary
    total_values = sum(word_count_dict.values())
    for key, value in word_count_dict.items():
        probs[key] = value / total_values

    return probs
