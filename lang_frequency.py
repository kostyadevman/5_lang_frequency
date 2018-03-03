import os
import re
import sys
from collections import Counter

COMMON_WORD_COUNT = 5

def load_data(filepath):
    with open(filepath, 'r') as infile:
        input_text = infile.read().lower()
    return input_text


def get_most_frequent_words(input_text):
    words = re.split('\W+', input_text)
    five_most_common_word = Counter(words).most_common(COMMON_WORD_COUNT)

    return five_most_common_word


if __name__ == '__main__':
    input_file = sys.argv[1]
    if os.path.exists(input_file):
        input_text = load_data(input_file)
        five_most_common_word = get_most_frequent_words(input_text)
        for word in five_most_common_word:
            print(word)
    else:
        print("file {} doesn't exists ".format(input_file))