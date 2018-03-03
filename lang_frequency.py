import os
import re
import sys


def load_data(filepath):
    with open(filepath, 'r') as infile:
       input_text = infile.read().lower()
    return input_text

def get_most_frequent_words(input_text):
    words = re.split('\W+', input_text)
    words_count = len(words)
    freq_words = {}

    for word in words:
        if word not in freq_words:
            freq_words[word] = words.count(word)

    freq_words_sorted = sorted(freq_words, key=freq_words.get, reverse=True)

    return freq_words_sorted

if __name__ == '__main__':
    input_file = sys.argv[1]
    if os.path.exists(input_file):
        input_text = load_data(input_file)
        freq_words_sorted = get_most_frequent_words(input_text)
        for word in freq_words_sorted[0:5]:
            print(word)

    else:
        print("file {} doesn't exists ".format(input_file))