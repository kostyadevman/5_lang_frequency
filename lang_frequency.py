import os
import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as infile:
        input_text = infile.read()
    return input_text


def get_most_frequent_words(input_text):
    common_word_count = 5
    input_text = input_text.lower()
    words = re.split('\W+', input_text)
    most_common_words = Counter(words).most_common(common_word_count)

    return most_common_words


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Usage: python lang_frequency.py <path to file')
    input_file = sys.argv[1]
    if os.path.exists(input_file):
        input_text = load_data(input_file)
        most_common_words = get_most_frequent_words(input_text)
        print('The most frequent word in {}: '.format(input_file))
        for word, count in most_common_words:
            print('word: {} - frequency: {}'.format(word, count))
    else:
        print("file {} doesn't exists ".format(input_file))